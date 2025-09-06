from django.contrib import admin

# Register your models here.
from .models import PostsModel
admin.site.register(PostsModel)