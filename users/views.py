# Create your views here.
from knox.auth import AuthToken
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.serializers import RegisterSerializer


@api_view(["POST"])
def login_api(request):
    serializer = AuthTokenSerializer(
        data=request.data
    )  # validate data from the request
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data["user"]
    _, token = AuthToken.objects.create(
        user
    )  # for getting the token created for user

    return Response(
        {
            "user_info": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            "token": token,
        }
    )


@api_view(["GET"])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response(
            {
                "user_info": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
            }
        )

    return Response(
        {"error": "not authenticated"}, status=status.HTTP_401_UNAUTHORIZED
    )


@api_view(["POST"])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()
    _, token = AuthToken.objects.create(user)

    return Response(
        {
            "user_info": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            "token": token,
        }
    )
