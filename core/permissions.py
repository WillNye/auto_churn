from rest_framework import permissions
"""
The Generic Permissions fall into 2 categories
Those a contact can access
And those that a contact cannot access
"""


class GenericAuthOrReadOnly(permissions.BasePermission):
    write_groups = []

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.id is None:
            return False
        elif len(self.write_groups) == 0:
            return True
        else:
            return any(user_group.name in self.write_groups for user_group in request.user.groups.all())


class GenericInternalPermissions(permissions.BasePermission):
    read_groups = []
    write_groups = []

    def has_permission(self, request, view):
        # Users must be logged in and must be staff
        if request.user.id is None or not request.user.is_staff:
            return False
        elif len(self.read_groups) == 0:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return any(user_group.name in self.read_groups for user_group in request.user.groups.all())
        elif len(self.write_groups) == 0:
            return True
        else:
            # Instance must have an attribute named `owner`.
            return any(user_group.name in self.write_groups for user_group in request.user.groups.all())


class CookifyBasePermissions(GenericAuthOrReadOnly):
    write_groups = []



