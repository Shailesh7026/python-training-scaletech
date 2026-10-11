from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View
import json
from users.models import User


class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            if not email or not password:
                return JsonResponse(
                    {"message": "Email and password are required"}, status=400
                )

            user = authenticate(
                request,
                email=email,
                password=password
            )

            if user is None:
                return JsonResponse(
                    {"message": "Invalid email or password"},
                    status=401
                )

            # Log the user in
            login(request, user)

            return JsonResponse(
                {
                    "message": "Login successful",
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "role": user.role.role_name if user.role else None,
                    },
                },
                status=200,
            )

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

class RegisterView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")
            first_name = data.get("first_name")
            last_name = data.get("last_name")

            if not email or not password:
                return JsonResponse(
                    {"message": "Email and password are required"}, status=400
                )

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message": "Email already exists"}, status=400)

            user = User.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )

            return JsonResponse(
                {
                    "message": "User registered successfully",
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                    },
                },
                status=201,
            )


        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
