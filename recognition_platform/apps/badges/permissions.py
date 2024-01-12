from rest_framework import permissions
from apps.auth0authorization.models import EmployeeInfo


class IsManagerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        employee_info = EmployeeInfo.objects.get(user=request.user)
        return employee_info.position == 'Group Manager'

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
