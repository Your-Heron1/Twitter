from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Profile(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=100, unique=True, primary_key=True)
    username = models.CharField(max_length=100)
    #token = Token.objects.create(user=Profile/get)
    first_name = None
    last_name = None
    last_login = models.CharField(max_length=100, blank=True, default=('None'))
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(verbose_name='E-mail', unique=True)
    bio = models.CharField(max_length=256, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Following(models.Model):

    user_id = models.ForeignKey(Profile, related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(Profile, related_name="followers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        unique_together = ("user_id", "following_user_id")
        ordering = ["-created"]

    def __str__(self):
        return f"{self.user_id} follows {self.following_user_id}"


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='poster')
    title = models.CharField(verbose_name='Заголовок', max_length=50, blank=True)
    text = models.TextField(verbose_name='Содержание')
    date_published = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)

    def __str__(self):
        return 'Author: {}, Title {}'.format(self.author, self.title)

    class Meta:
        ordering = ["-date_published"]