from unicodedata import name
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsAdmin

# register user api view
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# list users api view
class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# update user api view
class UpdateUserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticated, IsAdmin]

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

# Generate custom token with additional fields
class GenerateCustomToken(RefreshToken):
    @classmethod
    def for_user(cls, user):
        token = super().for_user(user)
        # Add custom claims
        token['phone'] = user.phone
        token['username'] = user.username
        token['is_staff'] = user.is_staff
        # token["user_id"] = user.id
        # token["user_type"] = user.user_type   # CUSTOMER / INTERNAL
        # token["role"] = user.role             # SALES / ADMIN / etc
        # token["is_super_admin"] = user.is_super_admin

        return token

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    def post(self, request):
       
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)

       username = serializer.validated_data['username']
       password = serializer.validated_data['password']

       user = User.objects.filter(username=username).first()
       if user is None or not user.check_password(password):
           return Response({'error': 'Invalid credentials'}, status=400)
       refresh = GenerateCustomToken.for_user(user)
       return Response({
           'refresh': str(refresh),
           'access': str(refresh.access_token),
       })


@api_view(['GET'])
def test_view(request):
    return Response({
        "register": "register/",
        "login": "login/",
        "login/refresh": "login/refresh/",
        "users": "users/"
    })