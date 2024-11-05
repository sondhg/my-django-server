import datetime

import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("User not found!")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        payload = {
            "id": user.id,
            "exp": datetime.datetime.now(datetime.timezone.utc)
            + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.now(datetime.timezone.utc),
        }

        token = jwt.encode(payload, "secret", algorithm="HS256")
        # this version of PyJWT already returns a string, so no need to decode it
        refresh_token = jwt.encode({"id": user.id, "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7)}, "secret", algorithm="HS256")

        user.refresh_token = refresh_token
        user.save()
        
        response = Response()

        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {
            "jwt": token,
            "refresh_token": refresh_token,
            "email": user.email,
            "name": user.name  # Assuming the User model has a 'name' field
        }

        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            raise AuthenticationFailed("Unauthenticated!")

        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")

        user = User.objects.filter(id=payload["id"]).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)


# views.py
class LogoutView(APIView):
    def post(self, request):
        email = request.data.get("email")
        refresh_token = request.data.get("refresh_token")

        user = User.objects.filter(email=email, refresh_token=refresh_token).first()
        if user is None:
            raise AuthenticationFailed("Invalid refresh token!")

        user.refresh_token = None
        user.save()

        response = Response()
        response.delete_cookie("jwt")
        response.data = {
            "message": "Successfully logged out"
        }

        return response
