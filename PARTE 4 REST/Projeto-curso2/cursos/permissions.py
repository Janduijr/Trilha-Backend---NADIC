from rest_framework import permissions

class EhSuperUsuario(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
                return True
        if request.user.is_superuser:
            return False
        return True