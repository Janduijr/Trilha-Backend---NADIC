from rest_framework import permissions

class EhSuperUsuario(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True