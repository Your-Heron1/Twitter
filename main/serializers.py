from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user_id', 'username', 'email', 'password')


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = ("user_id", "following_user_id", "created")


class FollowingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = '__all__'


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'