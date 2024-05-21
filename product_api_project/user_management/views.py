from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer
from .services import UserService
import json, bcrypt
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        try:
            email = request.data.get('email')
            fullname = request.data.get('fullname')
            password = request.data.get('password')
            user = UserService.register_user(email, fullname, password)
            
            user_dict = {
                'email': user.email,
                'fullname': user.fullname,
            }
            
            return Response({'message': 'User registered successfully', 'user': user_dict}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserAuthenticationView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        try:
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            # Retrieve email and password from the request body
            email = body_data.get('email')
            password = body_data.get('password')

            # Retrieve the user from the database
            user = User.objects.filter(email=email).first()

            # Check if the user exists and the password matches
            if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                # Generate JWT tokens
                refresh = RefreshToken.for_user(user)
                access = AccessToken.for_user(user)

                return Response({
                    'message': 'success',
                    'user': {
                        'email': user.email,
                        'fullname': user.fullname,
                    },
                    'access_token': str(access),
                    'refresh_token': str(refresh),
                }, status=200)
            else:
                return Response({'message': 'Invalid credentials', 'status': 401}, status=401)
        except Exception as e:
            return Response({'error': str(e), 'status': 500}, status=500)
