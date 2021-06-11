import json
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework import generics, permissions, status, authentication
from rest_framework.views import APIView

from .models import *
from .serializers import *


class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delite()
        return Response(status=status.HTTP_200_OK)


class PostCreateView(generics.ListCreateAPIView):
    serializer_class = PostDetailSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


@csrf_exempt
def PostList(request):
    posts = Post.objects.all()

    for item in posts:
        item = model_to_dict(item)
    posts_serializer = PostListSerializer(posts, many=True)
    return JsonResponse(posts_serializer.data, safe=False)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()