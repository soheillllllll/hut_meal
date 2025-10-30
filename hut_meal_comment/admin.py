from django.contrib import admin

# Register your models here.

from .models import CommentProduct, CommentBlog


# @admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(CommentProduct, CommentAdmin)
admin.site.register(CommentBlog, CommentAdmin)