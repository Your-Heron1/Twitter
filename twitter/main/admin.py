from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(Post)
admin.site.register(Profile, UserAdmin)
admin.site.register(Following)