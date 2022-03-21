# Create your views here.

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class GetUserView(APIView):
    permissions_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)