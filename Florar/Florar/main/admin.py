from django.contrib import admin

from.models import *

admin.site.register(portifolio)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_field = ('title', 'content')


admin.site.register(Post, PostAdmin)