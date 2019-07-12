from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model

)
from blogposts.models import blogPost

User = get_user_model()


class Profile(forms.ModelForm):
    class Meta:
        model = blogPost
        fields = ['profile_picture']


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not User.objects.filter(username=username):
                raise forms.ValidationError("This user doesn't exist.")

            elif not user:
                raise forms.ValidationError("Invalid Password.")

            if not user.is_active:
                raise forms.ValidationError("User is not active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [

            'username',
            'email',
            'password',
            'password2'

        ]

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("Password do not match.")
        user_qs = User.objects.filter(username = username)
        if user_qs.exists():
            raise forms.ValidationError("Username is already taken.")
        else:
            email_qs = User.objects.filter(email=email)
            if email_qs.exists():
                raise forms.ValidationError("This email is already in use.")
            else:
                return super(UserRegisterForm, self).clean(*args, **kwargs)



