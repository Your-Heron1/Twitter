from rest_framework import permissions, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *
from rest_framework.views import APIView


class UserFollowingViewSet(generics.ListAPIView):
    serializer_class = FollowingSerializer
    queryset = Following.objects.all()


class UserFollowingCreate(generics.ListCreateAPIView):
    serializer_class = FollowingDetailSerializer