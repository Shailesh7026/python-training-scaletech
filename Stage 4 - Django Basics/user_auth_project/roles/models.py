from django.db import models
from django.core.exceptions import ValidationError


# validators
def validate_access_modules(value):
    if not isinstance(value,list):
        raise ValidationError(
            ("%(value)s is not a valid list"),
            params={"value": value},
        )

    normalized = [item.strip().lower() for item in value]

    if any(not item for item in normalized):
        raise ValidationError(
            ("%(value)s contains empty strings"),
            params={"value": value},
        )

    if len(normalized) != len(set(normalized)):
        raise ValidationError(
            ("%(value)s contains duplicate values"),
            params={"value": value},
        )


class RoleQueySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)


class Role(models.Model):
    role_name = models.CharField(max_length=200, unique=True, blank=False)
    access_modules = models.JSONField(
        default=list, validators=[validate_access_modules], blank=True
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = RoleQueySet.as_manager()

    def check_module(self, module):
        if not isinstance(module, str):
            raise ValidationError("Module name must be a string.")

        module = module.strip().lower()

        return module in [
            item.strip().lower()
            for item in self.access_modules
        ]

    def add_module(self, module):
        module = module.strip().lower() if isinstance(module, str) else ""

        if not module:
            raise ValidationError("Module name cannot be empty.")

        if self.check_module(module):
            raise ValidationError(
                f"Module '{module}' already exists in access_modules."
            )

        self.access_modules.append(module)
        self.save()

    def remove_module(self, module):
        if not isinstance(module, str) or not module.strip():
            raise ValidationError("Module name must be a non-empty string.")

        module = module.strip().lower()

        if not self.check_module(module):
            raise ValidationError(
                f"Module '{module}' does not exist in access_modules."
            )

        self.access_modules = [
            item
            for item in self.access_modules
            if item.strip().lower() != module
        ]

        self.save()

    def __str__(self):
        return self.role_name
