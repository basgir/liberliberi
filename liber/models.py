from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# We define the file system storage
# Image file storage system
bo_img = FileSystemStorage(location='/home/bgir/Projects/4-prog-for-econ-101-web-app/website/courses/media/courses/img')


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=False)
    subscription_start = models.DateField()
    subscription_end = models.DateField()
    bio = models.TextField(max_length=500, blank=True)
    birthday = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(default='basic-slug',max_length=60)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    added = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.URLField()
    image = models.FileField(storage=co_img)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField(max_length=10000)
    resource = models.FileField(default = None)
    pub_date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=300)

    def __str__(self):
        return self.name
