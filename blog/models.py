from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.content
    
class Tag(models.Model):
    name=models.CharField(max_length=200)
    posts=models.ManyToManyField(Post)
    
    def __str__(self):
        return self.name
    