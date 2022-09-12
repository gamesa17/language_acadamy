from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from permissions.models import Permission
from permissions.serializers import PermissionSerializer


class PermissionsView(APIView):
    @staticmethod
    def get(request):
        try:
            user = request.user

            permissions = Permission.objects.filter(user=user)
            serializedPermissions = PermissionSerializer(data=permissions, many=True)

            if not serializedPermissions.is_valid():
                Response(
                    data={"error": "Невалидные права пользователя"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            return Response(
                data=(permission["key"] for permission in serializedPermissions.data),
                status=status.HTTP_200_OK,
            )

        except Exception as error:
            return Response(
                data={"error": str(error)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
