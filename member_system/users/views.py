from datetime import datetime

from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.token:
                user.token_expiry = timezone.now()
                user.save()

            refresh = RefreshToken.for_user(user)
            user.token = str(refresh.access_token)
            user.token_expiry = datetime.fromtimestamp(refresh.access_token.payload['exp'])

            user.save()

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
