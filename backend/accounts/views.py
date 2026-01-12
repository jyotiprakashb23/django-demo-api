from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from .models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

@api_view(['GET'])
def test_view(request):
    return Response({
        "register": "register/",
        "login": "login/",
        "login/refresh": "login/refresh/",
        "users": "users/"
    })