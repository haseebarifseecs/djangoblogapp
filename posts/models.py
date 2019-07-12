from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import  RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = RichTextUploadingField(blank=True, null=True
                                         ,external_plugin_resources=[(
            'youtube', '/static/vendor/ckeditorplugins/youtube_2.1.13/youtube/',
            'plugin.js',
        )])

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()


    def __str__(self):
        return self.title

