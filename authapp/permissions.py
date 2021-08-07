from rest_framework import permissions


class AnonCreateAndUpdateOwnerOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return view.action == 'create' or request.user and request.user.is_authenticated
