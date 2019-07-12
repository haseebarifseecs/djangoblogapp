
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import  static
from blogposts.views import index, blog, post, search, post_update, post_delete, post_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('posts.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', index),
    path('blogs/',blog, name='post_list'),
    path('post/<id>/', post, name='post_detail'),
    path('post/create',post_create, name='post_create'),
    path('post/<id>/update',post_update, name='post_update'),
    path('post/<id>/delete',post_delete, name='post_delete'),
    path('search/', search, name='search'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
