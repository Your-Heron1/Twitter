from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url

from . import views
from .views import *
from .viewsFollowing import *
from .viewsProfile import *


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),
    path('profile/create/', ProfileCreateView.as_view()),
    path('profile/all/', ProfileListView.as_view()),
    path('profile/detail/<int:pk>/', ProfileDetailView.as_view()),
    path('profile/<int:pk>/', views.Profile),
    path('post/add/', PostCreateView.as_view()),
    path('post/detail/<int:pk>/', PostDetailView.as_view()),
    path('post/all/', PostListView.as_view()),
    path('following/', UserFollowingViewSet.as_view()),
    path('following/add/', UserFollowingCreate.as_view()),
    url(r'^postsAll/', views.PostList),
]