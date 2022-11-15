from rest_framework import permissions



class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.creator__id==self.request.user.id