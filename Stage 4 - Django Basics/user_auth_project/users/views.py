from django.core.paginator import EmptyPage, Paginator
from django.db.models.functions import JSONObject
from django.http.response import JsonResponse
from django.shortcuts import render
import json

from django.views import View
from .models import User
from roles.models import Role
from authentication.permissions import has_module_access


class UserView(View):
    def authenticate_user(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({"message": "Authentication required"}, status=401)

        if not has_module_access(request.user, "manage_users"):
            return JsonResponse({"message": "You don't have permission"}, status=403)

    def get(self, request, user_id=None):

        auth_response = self.authenticate_user(request)
        if auth_response:
            return auth_response

        # Get user by ID
        if user_id is not None:
            user = (
                User.objects.filter(id=user_id, is_active=True)
                .values(
                    "id",
                    "email",
                    "first_name",
                    "last_name",
                    role_data=JSONObject(
                        id="role__id",
                        role_name="role__role_name",
                        access_modules="role__access_modules",
                    ),
                )
                .first()
            )

            if not user:
                return JsonResponse({"message": "User not found"}, status=404)

            return JsonResponse(
                {"message": "User fetched successfully", "user": user}, status=200
            )

        # Get user list
        page = request.GET.get("page", 1)
        limit = request.GET.get("limit", 10)

        try:
            page = int(page)
            limit = int(limit)

            if page < 1 or limit < 1 or limit > 100:
                raise ValueError()

        except (ValueError, TypeError):
            return JsonResponse(
                {
                    "message": "Page and limit must be positive integers. Maximum limit is 100."
                },
                status=400,
            )

        users = (
            User.objects.filter(is_active=True)
            .order_by("id")
            .values(
                "id",
                "email",
                "first_name",
                "last_name",
                role_data=JSONObject(
                    id="role__id",
                    role_name="role__role_name",
                    access_modules="role__access_modules",
                ),
            )
        )

        paginator = Paginator(users, limit)

        try:
            page_obj = paginator.page(page)

        except EmptyPage:
            return JsonResponse({"message": "Page does not exist"}, status=404)

        return JsonResponse(
            {
                "message": "User list fetched successfully",
                "users": list(page_obj),
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
        try:
            auth_response = self.authenticate_user(request)
            if auth_response:
                return auth_response

            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")
            first_name = data.get("first_name")
            last_name = data.get("last_name")

            if not email or not password:
                return JsonResponse(
                    {"message": "Email and password are required"}, status=400
                )

            if User.objects.filter(email__iexact=email).exists():
                return JsonResponse({"message": "Email already exists"}, status=400)

            role = None

            if data.get("role") is not None:
                try:
                    role = Role.objects.get(id=int(data["role"]), is_active=True)
                except (Role.DoesNotExist, ValueError, TypeError):
                    return JsonResponse(
                        {"message": "Invalid or inactive role"}, status=400
                    )

            user = User(
                email=email,
                first_name=first_name,
                last_name=last_name,
                role=role,
            )

            user.set_password(password)
            user.full_clean()
            user.save()

            return JsonResponse(
                {
                    "message": "User created successfully",
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "role": user.role.role_name if user.role else None,
                    },
                },
                status=201,
            )

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def put(self, request, user_id):

        try:
            auth_response = self.authenticate_user(request)
            if auth_response:
                return auth_response

            data = json.loads(request.body)

            if not isinstance(data, dict):
                return JsonResponse(
                    {"message": "Request body must be a JSON object"}, status=400
                )

            user = User.objects.select_related("role").filter(id=user_id).first()

            if not user:
                return JsonResponse({"message": "User not found"}, status=404)

            if "first_name" in data:
                if not isinstance(data["first_name"], str):
                    return JsonResponse(
                        {"message": "First name must be a string"}, status=400
                    )

                user.first_name = data["first_name"]

            if "last_name" in data:
                if not isinstance(data["last_name"], str):
                    return JsonResponse(
                        {"message": "Last name must be a string"}, status=400
                    )

                user.last_name = data["last_name"]

            if "email" in data:
                email = data["email"]

                if not isinstance(email, str) or not email.strip():
                    return JsonResponse({"message": "Invalid email"}, status=400)

                email = email.strip()

                if (
                    User.objects.filter(email__iexact=email)
                    .exclude(id=user_id)
                    .exists()
                ):
                    return JsonResponse({"message": "Email already exists"}, status=409)

                user.email = email

            if "role" in data:
                if data["role"] is None:
                    user.role = None

                else:
                    try:
                        user.role = Role.objects.get(
                            id=int(data["role"]), is_active=True
                        )

                    except (Role.DoesNotExist, ValueError, TypeError):
                        return JsonResponse(
                            {"message": "Invalid or inactive role"}, status=400
                        )

            if "is_active" in data:
                if not isinstance(data["is_active"], bool):
                    return JsonResponse(
                        {"message": "is_active must be a boolean"}, status=400
                    )

                user.is_active = data["is_active"]

            user.full_clean()
            user.save()

            return JsonResponse(
                {
                    "message": "User updated successfully",
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "role": {
                            "id": user.role.id,
                            "role_name": user.role.role_name,
                            "access_modules": user.role.access_modules,
                        }
                        if user.role
                        else None,
                        "is_active": user.is_active,
                    },
                },
                status=200,
            )

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def delete(self, request, user_id):

        auth_response = self.authenticate_user(request)
        if auth_response:
            return auth_response

        if not user_id:
            return JsonResponse({"message": "User ID is required"}, status=400)

        user = User.objects.filter(id=user_id).first()

        if not user:
            return JsonResponse({"message": "User not found"}, status=404)

        user.delete()

        return JsonResponse({"message": "User deleted successfully"}, status=200)
