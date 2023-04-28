from django.contrib import admin
from .models import Post, Comment, Blogger

# admin.site.register(Post)
# admin.site.register(Comment)
# admin.site.register(Blogger)

class BloggerAdmin(admin.ModelAdmin):
    list_display = ('name', 'username')

    fieldsets = (
        ('Identification', {
                'fields': ('name', 'birth', 'username')
    }),
        ('Bio info', {
                'fields': ('bio',)
        }),
    )

admin.site.register(Blogger, BloggerAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'date')
    list_filter = ('author', 'date')

admin.site.register(Comment, CommentAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'date')
    list_filter = ('author', 'date')

admin.site.register(Post, PostAdmin)
