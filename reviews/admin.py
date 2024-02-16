from django.contrib import admin
from .models import Comment
from .models import Rating

admin.site.register(Comment)
admin.site.register(Rating)
