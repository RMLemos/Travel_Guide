from django.contrib import admin
from reviews.actions import refuse_comment, approve_comment
from .models import Comment
from .models import Rating


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment', 'approved']
    actions = [refuse_comment, approve_comment]

admin.site.register(Comment, CommentAdmin)
admin.site.register(Rating)
