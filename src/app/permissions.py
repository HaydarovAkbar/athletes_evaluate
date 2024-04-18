from rest_framework import permissions

class MainRefereeAccessPermession(permissions.BasePermission):
    message="Creating a new match not allowed."

    def has_permission(self, request, view):
        if request.user.main==True:
            return True
