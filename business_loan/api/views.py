from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import UserProfile, BusinessDetails, LoanApplication
from .serializers import *


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserProfileView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

class BusinessDetailsView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BusinessDetailsSerializer

class LoanApplicationView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LoanApplicationSerializer

    def get_queryset(self):
        return LoanApplication.objects.filter(user=self.request.user)

# New endpoints for existence check
from rest_framework.views import APIView
from rest_framework.response import Response

class ProfileExistsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        exists = UserProfile.objects.filter(user=request.user).exists()
        return Response({"exists": exists})

class BusinessExistsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        exists = BusinessDetails.objects.filter(user=request.user).exists()
        return Response({"exists": exists})
