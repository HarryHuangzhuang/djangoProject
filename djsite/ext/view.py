from rest_framework.views import APIView


class NbAPIView(APIView):
    def check_permissions(self, request):
        Permission_objects = self.get_permissions()
        no_permission_objects = []

        for permission in Permission_objects:
            if permission.has_permission(request, self):
                return
            else:
                no_permission_objects.append(permission)

        else:
            self.permission_denied(
                request,
                message=getattr(no_permission_objects[0], "message", None),
                code=getattr(no_permission_objects[0], "code", None),
            )
