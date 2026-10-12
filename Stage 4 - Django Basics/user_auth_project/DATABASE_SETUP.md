# Database Setup

## 1. Check the configured database

Open `user_auth_project/settings.py` and inspect `DATABASES`.

A standard Django SQLite configuration looks like:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

If this is your configuration, SQLite is ready for local development and does not require a separate database server.

## 2. Initialize SQLite

From the directory containing `manage.py`, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

Django creates the database file at the path specified by `DATABASES["default"]["NAME"]`.

## 3. Custom user model and migrations

The project uses:

```python
AUTH_USER_MODEL = "users.User"
```


Useful commands:

```bash
python manage.py showmigrations
python manage.py makemigrations
python manage.py migrate
```

## 4. Create an administrator

After migrations:

```bash
python manage.py createsuperuser
```

The custom user model uses email as `USERNAME_FIELD`.

## 5. Verify database setup

```bash
python manage.py check
python manage.py showmigrations
```

