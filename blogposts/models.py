from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor_uploader.fields import  RichTextUploadingField

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('blogPost', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class blogPost(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField(blank=True, null=True
                                         , external_plugin_resources=[(
            'youtube', '/static/vendor/ckeditorplugins/youtube_2.1.13/youtube/',
            'plugin.js',
        )])
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={
            'id': self.id
        })

    def get_update_url(self):
        return reverse('post_update', kwargs={
            'id': self.id
        })

    def get_delete_url(self):
        return reverse('post_delete', kwargs={
            'id': self.id
        })

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()
