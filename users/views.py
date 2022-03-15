# Create your views here.

import datetime

import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import RegisterSerializer

from .models import User


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("user not found")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload, "secrect", algorithm="HS256").decode(
            "utf-8"
        )

        response = Response()

        response.set_cookies(key="jwt", value=token, httponly=True)
        response.data = {"jwt": token}
        return response
