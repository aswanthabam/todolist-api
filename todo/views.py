from django.contrib.auth import get_user_model
from rest_framework import views, permissions, status,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *
from .authentication import JWTAuthentication

User = get_user_model()

class UserRegistrationView(viewsets.ModelViewSet):
  queryset = CustomUser.objects.all()
  # permission_classes = [permissions.AllowAny]
  serializer_class = UserSerializer
  
  #def post(self, request, *args, **kwargs):
  #     serializer = self.serializer_class(data=request.data)
  #      serializer.is_valid(raise_exception=True)
        
  #      username = serializer.validated_data.get('username')
  #      first_name = serializer.validated_data.get('first_name')
  #      second_name = serializer.validated_data.get('second_name')
  #      email = serializer.validated_data.get('email')
  #      password  = serializer.validated_data.get('password ')
 
 
# AUTHORIZATION: Bearer <TOKEN>
class ObtainTokenView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ObtainTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username_or_phone_number = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = User.objects.filter(username=username_or_phone_number).first()
        # print(user.check_password(password),password,user.password)
        if user is None or not user.password== password:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate the JWT token
        jwt_token = JWTAuthentication.create_jwt(user)

        return Response({'token': jwt_token})