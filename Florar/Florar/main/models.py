from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


class portifolio(models.Model):
    title=models.CharField(max_length=400)
    image=models.ImageField(upload_to="portifolio_imgs/")
    slug=models.CharField(max_length=800)
    detail=models.TextField()
    status=models.BooleanField(default=True)



    def __str__(self):
        return self.title

STATUS = ((0, 'Draft'), (1,'Published'))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateField(auto_now_add=True)
    update_on = models.DateField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering = ['-created_on']

def __str__(self):
    return self.title