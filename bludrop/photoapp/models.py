from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    #photo = models.ImageField(upload_to='img')

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.CharField(max_length=255,null=True)
    photo = models.ForeignKey(Photo,on_delete=models.CASCADE,related_name='comment')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')


    def __str__(self):
        return self.comment

