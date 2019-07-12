from django import forms
from .models import blogPost
from django.contrib.auth.models import User


class blogPostCreationForm(forms.ModelForm):
    class Meta:
        model = blogPost
        fields = ('title', 'overview', 'content', 'thumbnail', 'categories',
                  'featured', 'previous_post', 'next_post', 'profile_picture')

        def clean_author(self):
            if not self.cleaned_data['author']:
                return User()
            return self.cleaned_data['author']
