import json
from django.core.paginator import EmptyPage, Paginator
from django.db.models import ProtectedError
from django.http import JsonResponse
from django.views import View
from .models import Role
from authentication.permissions import has_module_access
from django.core.exceptions import ValidationError


class RoleView(View):
    def authenticate_user(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({"message": "Authentication required"}, status=401)

        if not has_module_access(request.user, "manage_roles"):
            return JsonResponse({"message": "You don't have permission"}, status=403)

    def get(self, request, role_id=None):
        try:
            auth_response = self.authenticate_user(request)
            if auth_response:
                return auth_response

            # get role by id
            if role_id:
                role = (
                    Role.objects.filter(id=role_id, is_active=True)
                    .values("id", "role_name", "access_modules")
                    .first()
                )
                if not role:
                    return JsonResponse({"message": "Role not found"}, status=404)

                return JsonResponse(
                    {"message": "Role fetched successfully", "role": role}, status=200
                )

            # get list of roles
            page = request.GET.get("page", 1)
            limit = request.GET.get("limit", 10)

            try:
                page = int(page)
                limit = int(limit)

                if page < 1 or limit < 1:
                    raise ValueError("Page and limit must be positive integers")

                if limit > 100:
                    raise ValueError("Limit cannot exceed 100")

            except ValueError:
                return JsonResponse(
                    {"message": "Page and limit must be integers"}, status=400
                )

            roles = (
                Role.objects.filter(is_active=True)
                .order_by("id")
                .values("id", "role_name", "access_modules")
            )

            paginator = Paginator(roles, limit)

            try:
                page_obj = paginator.page(page)
            except EmptyPage:
                return JsonResponse({"message": "Page not found"}, status=404)

            return JsonResponse(
                {
                    "message": "Role list fetched successfully",
                    "roles": list(page_obj),
                    "pagination": {
                        "page": page_obj.number,
                        "limit": limit,
                        "total_pages": paginator.num_pages,
                        "total_records": paginator.count,
                    },
                },
                status=200,
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def post(self, request):
        try:
            auth_response = self.authenticate_user(request)
            if auth_response:
                return auth_response

            data = json.loads(request.body)
            role_name = data.get("role_name")
            access_modules = data.get("access_modules", [])

            if not role_name or not isinstance(role_name, str) or not role_name.strip():
                return JsonResponse({"message": "Role name is required"}, status=400)

            if Role.objects.filter(role_name__iexact=role_name).exists():
                return JsonResponse({"message": "Role name already exists"}, status=400)

            role = Role(
                role_name=role_name,
                access_modules=access_modules,
            )

            role.full_clean()  # Validate the model fields
            role.save()

            return JsonResponse(
                {
                    "message": "Role created successfully",
                    "role": {
                        "id": role.id,
                        "role_name": role.role_name,
                        "access_modules": role.access_modules,
                    },
                },
                status=201,
            )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except ValidationError as e:
            return JsonResponse(
                {
                    "message": "Validation failed",
                    "errors": (
                        e.message_dict if hasattr(e, "message_dict") else e.messages
                    ),
                },
                status=400,
            )

    def put(self, request, role_id):
        try:
            auth_response = self.authenticate_user(request)
            if auth_response:
                return auth_response

            data = json.loads(request.body)

            role = Role.objects.filter(id=role_id).first()

            if not role:
                return JsonResponse({"message": "Role not found"}, status=404)

            # Update role name
            if "role_name" in data:
                role_name = data["role_name"]

                if not isinstance(role_name, str) or not role_name.strip():
                    return JsonResponse(
                        {"message": "Role name cannot be empty"}, status=400
                    )

                role_name = role_name.strip()

                if (
                    Role.objects.filter(role_name__iexact=role_name)
                    .exclude(id=role_id)
                    .exists()
                ):
                    return JsonResponse(
                        {"message": "Role name already exists"}, status=409
                    )

                role.role_name = role_name

            # Update access modules
            if "access_modules" in data:
                role.access_modules = data["access_modules"]

            # Update active status
            if "is_active" in data:
                if not isinstance(data["is_active"], bool):
                    return JsonResponse(
                        {"message": "is_active must be a boolean"}, status=400
                    )

                role.is_active = data["is_active"]

            # Run model validation
            role.full_clean()

            # Save updated role
            role.save()

            return JsonResponse(
                {
                    "message": "Role updated successfully",
                    "role": {
                        "id": role.id,
                        "role_name": role.role_name,
                        "access_modules": role.access_modules,
                        "is_active": role.is_active,
                    },
                },
                status=200,
            )

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        except ValidationError as e:
            return JsonResponse(
                {
                    "message": "Validation failed",
                    "errors": (
                        e.message_dict if hasattr(e, "message_dict") else e.messages
                    ),
                },
                status=400,
            )

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def delete(self, request, role_id):
        try:
            auth_response = self.authenticate_user(request)
            if auth_response:
                return auth_response

            role = Role.objects.filter(id=role_id).first()
            if not role:
                return JsonResponse({"message": "Role not found"}, status=404)

            role.delete()

            return JsonResponse({"message": "Role deleted successfully"}, status=200)

        except ProtectedError:
            return JsonResponse(
                {"message": "Cannot delete this role because users are assigned to it"},
                status=409,
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
