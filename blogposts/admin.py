from django.contrib import admin

from .models import  Category, blogPost, PostView
from .forms import blogPostCreationForm

# admin.site.register(Author)
admin.site.register(Category)
admin.site.register(blogPost)
admin.site.register(PostView)

class blogPostAdmin(admin.ModelAdmin):
    form = blogPostCreationForm
    list_display = ('title', 'overview', 'content', 'thumbnail', 'categories',
                    'featured', 'previous_post', 'next_post', 'author')

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        obj.save()