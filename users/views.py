# users/views.py
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer

# Register API View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,) # Allow anyone to register
    serializer_class = RegisterSerializer

# Get User API View (Example of a protected endpoint)
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,) # Only authenticated users can access
    serializer_class = UserSerializer

    # Override get_object to return the currently authenticated user
    def get_object(self):
        return self.request.user