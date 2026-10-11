import json

from django.http import JsonResponse
from django.views import View
from django.core.paginator import Paginator, EmptyPage
from django.db import IntegrityError

from .models import Student
from users.models import User

from authentication.permissions import has_module_access


class StudentView(View):
    def get(self, request, student_id=None):

        if not request.user.is_authenticated:
            return JsonResponse({"message": "Authentication required"}, status=401)

        can_view_all = has_module_access(request.user, "students.view")
        can_view_own = has_module_access(request.user, "students.view_own")

        if not can_view_all and not can_view_own:
            return JsonResponse(
                {"message": "You don't have permission to view students"}, status=403
            )

        students = Student.objects.select_related("user").order_by("id")

        # Restrict student users to their own profile
        if not can_view_all:
            students = students.filter(user=request.user)

        students = students.values(
            "id",
            "user__id",
            "user__email",
            "user__first_name",
            "user__last_name",
            "roll_number",
            "age",
            "course",
        )

        # Get a single student
        if student_id is not None:
            student = students.filter(id=student_id).first()

            if not student:
                return JsonResponse({"message": "Student not found"}, status=404)

            return JsonResponse(
                {"message": "Student fetched successfully", "student": student},
                status=200,
            )

        # Pagination
        try:
            page = int(request.GET.get("page", 1))
            limit = int(request.GET.get("limit", 10))

            if page < 1 or limit < 1:
                raise ValueError

            limit = min(limit, 100)

        except (ValueError, TypeError):
            return JsonResponse({"message": "Invalid page or limit"}, status=400)

        paginator = Paginator(students, limit)

        try:
            page_obj = paginator.page(page)

        except EmptyPage:
            return JsonResponse({"message": "Page does not exist"}, status=404)

        return JsonResponse(
            {
                "message": "Students fetched successfully",
                "students": list(page_obj),
                "pagination": {
                    "page": page_obj.number,
                    "limit": limit,
                    "total_pages": paginator.num_pages,
                    "total_records": paginator.count,
                },
            },
            status=200,
        )

    def post(self, request):

        if not request.user.is_authenticated:
            return JsonResponse({"message": "Authentication required"}, status=401)

        if not has_module_access(request.user, "students.create"):
            return JsonResponse(
                {"message": "You don't have permission to create students"}, status=403
            )

        try:
            data = json.loads(request.body)

            if not isinstance(data, dict):
                return JsonResponse({"message": "Invalid request body"}, status=400)

            user_id = data.get("user_id")
            roll_number = data.get("roll_number")
            age = data.get("age")
            course = data.get("course")

            if user_id is None or not roll_number or age is None or not course:
                return JsonResponse({"message": "All fields are required"}, status=400)

            try:
                student_user = User.objects.select_related("role").get(
                    id=user_id, is_active=True
                )
            except User.DoesNotExist:
                return JsonResponse(
                    {"message": "Student user account not found"}, status=404
                )

            if not has_module_access(student_user, "students.view_own"):
                return JsonResponse(
                    {"message": "Selected user does not have a student role"},
                    status=400,
                )

            try:
                age = int(age)

                if age <= 0:
                    raise ValueError

            except (ValueError, TypeError):
                return JsonResponse(
                    {"message": "Age must be a positive integer"}, status=400
                )

            student = Student(
                user=student_user,
                roll_number=roll_number.strip(),
                age=age,
                course=course.strip(),
            )

            student.full_clean()
            student.save()

            return JsonResponse(
                {
                    "message": "Student created successfully",
                    "student": {
                        "id": student.id,
                        "user_id": student.user_id,
                        "email": student.user.email,
                        "roll_number": student.roll_number,
                        "age": student.age,
                        "course": student.course,
                    },
                },
                status=201,
            )

        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)

        except IntegrityError:
            return JsonResponse(
                {"message": "Student profile or roll number already exists"}, status=409
            )

    def put(self, request, student_id):

        if not request.user.is_authenticated:
            return JsonResponse({"message": "Authentication required"}, status=401)

        if not has_module_access(request.user, "students.update"):
            return JsonResponse(
                {"message": "You don't have permission to update students"}, status=403
            )

        try:
            data = json.loads(request.body)

            if not isinstance(data, dict):
                return JsonResponse({"message": "Invalid request body"}, status=400)

            student = (
                Student.objects.select_related("user").filter(id=student_id).first()
            )

            if not student:
                return JsonResponse({"message": "Student not found"}, status=404)

            if "roll_number" in data:
                if (
                    not isinstance(data["roll_number"], str)
                    or not data["roll_number"].strip()
                ):
                    return JsonResponse({"message": "Invalid roll number"}, status=400)
                student.roll_number = data["roll_number"].strip()

            if "age" in data:
                try:
                    age = int(data["age"])
                    if age <= 0:
                        raise ValueError
                    student.age = age
                except (ValueError, TypeError):
                    return JsonResponse(
                        {"message": "Age must be a positive integer"}, status=400
                    )

            if "course" in data:
                if not isinstance(data["course"], str) or not data["course"].strip():
                    return JsonResponse({"message": "Invalid course"}, status=400)
                student.course = data["course"].strip()

            student.save()

            return JsonResponse(
                {
                    "message": "Student updated successfully",
                    "student": {
                        "id": student.id,
                        "roll_number": student.roll_number,
                        "age": student.age,
                        "course": student.course,
                        "email": student.user.email,
                    },
                },
                status=200,
            )

        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)

        except IntegrityError:
            return JsonResponse({"message": "Roll number already exists"}, status=409)

    def delete(self, request, student_id):

        if not request.user.is_authenticated:
            return JsonResponse({"message": "Authentication required"}, status=401)

        if not has_module_access(request.user, "students.delete"):
            return JsonResponse(
                {"message": "You don't have permission to delete students"}, status=403
            )

        student = Student.objects.filter(id=student_id).first()

        if not student:
            return JsonResponse({"message": "Student not found"}, status=404)

        student.delete()

        return JsonResponse({"message": "Student deleted successfully"}, status=200)
