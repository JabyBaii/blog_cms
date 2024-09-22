from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [AllowAny]  # 允许任何人注册

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            logger.info(f"User created: {serializer.data['username']}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"User creation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def user_management_page(request):
    return render(request, 'user_management.html')