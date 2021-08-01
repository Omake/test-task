from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class TestView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_class = [AllowAny]

    def get(self, request):
        return Response({"test":"success"})
