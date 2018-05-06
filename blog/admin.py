from django.contrib import admin
from .models import Post
from .models import Category, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)

