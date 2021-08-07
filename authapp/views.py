from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from authapp.permissions import AnonCreateAndUpdateOwnerOnly
from authapp.serializers import UserSerializer


class UserApiView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AnonCreateAndUpdateOwnerOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
