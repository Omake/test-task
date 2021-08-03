from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from authapp.serializers import ReadOnlyUserSerializer, WriteOnlyUserSerializer


class UserApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=False):
        """Returns a list of users"""
        if pk:
            user = get_object_or_404(User, pk=pk)
            serializer = ReadOnlyUserSerializer(user)

            return Response(serializer.data, status=status.HTTP_200_OK)

        users = User.objects.all()
        serializer = ReadOnlyUserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create user"""
        write_serializer = WriteOnlyUserSerializer(data=request.data)
        if write_serializer.is_valid():
            created_user = write_serializer.save()
            read_serializer = ReadOnlyUserSerializer(created_user)

            return Response(read_serializer.data, status=status.HTTP_201_CREATED)

        return Response(write_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """Update user"""
        user = get_object_or_404(User, pk=pk)
        write_serializer = WriteOnlyUserSerializer(user, data=request.data)
        read_serializer = ReadOnlyUserSerializer(user)
        if write_serializer.is_valid():
            write_serializer.save()

            return Response(read_serializer.data, status=status.HTTP_201_CREATED)

        return Response(write_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """Update user"""
        user = get_object_or_404(User, pk=pk)
        write_serializer = WriteOnlyUserSerializer(user, data=request.data)
        read_serializer = ReadOnlyUserSerializer(user)
        if write_serializer.is_valid():
            write_serializer.save()

            return Response(read_serializer.data, status=status.HTTP_201_CREATED)

        return Response(write_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, pk):
        """Deactivate user"""
        user = get_object_or_404(User, pk=pk)
        user.is_active = False
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
