from rest_framework import permissions

class KotibHasAccessPermisson(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_kotib==True:
            return True
        
        