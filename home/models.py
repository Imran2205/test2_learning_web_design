from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

'''class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home-home')'''



class Post(models.Model):
    title = models.CharField(max_length=100)
    head1 = models.TextField(null=True, blank=True)
    content1 = models.TextField(null=True, blank=True)

    head2 = models.TextField(null=True, blank=True)
    content2 = models.TextField(null=True, blank=True)

    head3 = models.TextField(null=True, blank=True)
    content3 = models.TextField(null=True, blank=True)

    head4 = models.TextField(null=True, blank=True)
    content4 = models.TextField(null=True, blank=True)

    head5 = models.TextField(null=True, blank=True)
    content5 = models.TextField(null=True, blank=True)

    head6 = models.TextField(null=True, blank=True)
    content6 = models.TextField(null=True, blank=True)

    head7 = models.TextField(null=True, blank=True)
    content7 = models.TextField(null=True, blank=True)

    head8 = models.TextField(null=True, blank=True)
    content8 = models.TextField(null=True, blank=True)

    head9 = models.TextField(null=True, blank=True)
    content9 = models.TextField(null=True, blank=True)

    head10 = models.TextField(null=True, blank=True)
    content10 = models.TextField(null=True, blank=True)

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home-blog')#,kwargs={'pk':self.pk})


class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/', blank = True, null = True)
    image2 = models.ImageField(upload_to='photos/', blank=True, null=True)
    image3 = models.ImageField(upload_to='photos/', blank=True, null=True)
    image4 = models.ImageField(upload_to='photos/', blank=True, null=True)
    image5 = models.ImageField(upload_to='photos/', blank=True, null=True)
    image6 = models.ImageField(upload_to='photos/', blank=True, null=True)
    image7 = models.ImageField(upload_to='photos/', blank=True, null=True)
    image8 = models.ImageField(upload_to='photos/', blank=True, null=True)
    image9 = models.ImageField(upload_to='photos/', blank=True, null=True)
    image10 = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.post.title + "image"
