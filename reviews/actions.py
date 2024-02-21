def refuse_comment(modeladmin, request, queryset):
    queryset.update(approved=False)


def approve_comment(modeladmin, request, queryset):
    queryset.update(approved=True)


refuse_comment.short_description = 'Refuse comments'
approve_comment.short_description = 'Approve comments'