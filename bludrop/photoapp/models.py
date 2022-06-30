from django.db import models

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    photo = models.ImageField(upload_to='img')

    def __str__(self):
        return self.name
