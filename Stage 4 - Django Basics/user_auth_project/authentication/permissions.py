
def has_module_access(user, module):

    if not user or not user.is_authenticated:
        return False

    # Django superusers have unrestricted access
    if user.is_superuser:
        return True

    if not user.role:
        return False

    if not user.role.is_active:
        return False

   
    modules = user.role.access_modules or []
    modules = [
        item.strip().lower()
        for item in modules
        if isinstance(item, str)
    ]

    return module.strip().lower() in modules
