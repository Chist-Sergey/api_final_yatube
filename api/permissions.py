from rest_framework import permissions

good_stuff = ('GET', 'HEAD', 'OPTIONS')

class IsAuthorOrReadOnlyPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in good_stuff or
            request.user == obj.author
        )