from django.contrib import admin
from API.models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)
