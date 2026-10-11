# Django RBAC User Management API

This is a simple Django project demonstrating email-based authentication, role-based access control (RBAC), user management, role management, and resource management (i have used students to demonstrate the role based access like teacher , student.). 

i created use Django class-based views, the ORM, sessions, and `JsonResponse`;

## Features

- Session-based login.
- Role CRUD with JSON-based access-module validation.
- Module-level RBAC permissions so that specific user role can access resources (students records).
- User CRUD with role assignment.
- Student profiles linked to user accounts.
- Student ownership restriction: student users can view their own profile.
- Pagination for list endpoints where implemented.
- Input validation and appropriate HTTP error responses.

## Technology

| Technology | Purpose |
|---|---|
| Python 3.14.7 | Version used during development |
| Django 6.1.1 | Web framework |
| django-tailwind | Tailwind integration, if enabled in project settings | (currently not using it - just for future ui build)
| SQLite | Local database |
| Postman | API testing |

## Project Structure

```text
user_auth_project/
├── manage.py
├── requirements.txt
├── example.env
├── README.md
├── DATABASE_SETUP.md
├── user_auth_project/
│   ├── settings.py
│   └── urls.py
├── authentication/
│   ├── views.py
│   ├── urls.py
│   └── permissions.py
├── users/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── roles/
│   ├── models.py
│   ├── views.py
│   └── urls.py
└── students/
    ├── models.py
    ├── views.py
    └── urls.py
```

### App responsibilities

- `authentication/` — login and registration endpoints + shared permission-checking logic.
- `users/` — custom User model, user manager, and user CRUD APIs.
- `roles/` — Role model, access-module validation, and role CRUD APIs.
- `students/` — Student profile model and CRUD APIs with ownership restrictions.
- `user_auth_project/` — project settings and root URL configuration.
- `manage.py` — Django command-line utility.

## API Route Overview

The root URL configuration mounts these apps under `/api/v1/`.

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/v1/auth/login/` | Log in with email and password |
| POST | `/api/v1/auth/register/` | Register a user, if enabled |
| GET | `/api/v1/roles/` | List roles |
| GET | `/api/v1/roles/<role_id>/` | Retrieve a role |
| POST | `/api/v1/roles/` | Create a role |
| PUT | `/api/v1/roles/<role_id>/` | Update a role |
| DELETE | `/api/v1/roles/<role_id>/` | Delete a role |
| GET | `/api/v1/users/` | List users |
| GET | `/api/v1/users/<user_id>/` | Retrieve a user |
| POST | `/api/v1/users/` | Create a user |
| PUT | `/api/v1/users/<user_id>/` | Update a user |
| DELETE | `/api/v1/users/<user_id>/` | Delete a user |
| GET | `/api/v1/students/` | List students allowed by permissions |
| GET | `/api/v1/students/<student_id>/` | Retrieve a student allowed by permissions |
| POST | `/api/v1/students/` | Create a student profile |
| PUT | `/api/v1/students/<student_id>/` | Update a student profile |
| DELETE | `/api/v1/students/<student_id>/` | Delete a student profile |

pass paginated parameters as -- `?page=1&limit=10`.

## Running Locally

### 1. Open the project directory

```bash
cd user_auth_project
```

Run commands from the directory containing `manage.py`.

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Use `python -m pip` to install packages into the same Python environment used to run Django.

### 4. Configure environment variables

Copy `example.env` to `.env` and update its values:

```powershell
Copy-Item example.env .env
```

Django does not load `.env` automatically. Your `settings.py` must explicitly load the file (for example, using `python-dotenv` or `django-environ`) before these variables have any effect. Never commit a real `.env` file or production credentials.

### 5. Apply migrations

```bash
python manage.py migrate
```

If you have changed models and need new migration files:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

The custom user model uses email as its login identifier.

### 7. Start the development server

```bash
python manage.py runserver
```

- API base URL: `http://127.0.0.1:8000/`
- Django Admin: `http://127.0.0.1:8000/admin/`

## Authentication and Postman Testing

you can import "Django RBAC - Users, Roles & Students.postman_collection.json" to your postman and continue the testing 



