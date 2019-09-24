from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile
from home.models import Post, Images
#from home.models import Photo

'''class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file', )'''


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']


class ImageForm(forms.ModelForm):

    class Meta:
        model = Images
        fields = ['image', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9', 'image10']

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title',
                  'head1', 'content1',
                  'head2', 'content2',
                  'head3', 'content3',
                  'head4', 'content4',
                  'head5', 'content5',
                  'head6', 'content6',
                  'head7', 'content7',
                  'head8', 'content8',
                  'head9', 'content9',
                  'head10', 'content10']