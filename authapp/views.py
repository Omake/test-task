from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class UserApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_class = [AllowAny]

    def get(self, request):
        """Returns a list of users"""
        users = User.objects.all()

        return Response(users)

    def post(self):
        pass


