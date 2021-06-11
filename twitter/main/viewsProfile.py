from rest_framework import generics, request
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from .models import *
from .serializers import *
from .views import *


class ProfileCreateView(generics.ListCreateAPIView):
    serializer_class = ProfileDetailSerializer


class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileListSerializer
    queryset = Profile.objects.all()


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileDetailSerializer
    queryset = Profile.objects.all()


class Profile(generics.ListAPIView):
    def get_queryset(self, request, pk):
        follow_query = Following.objects.filter(user_id=pk)
        serializer_class = PostListSerializer
        queryset = Post.objects.filter(author=follow_query.following_user_id)





