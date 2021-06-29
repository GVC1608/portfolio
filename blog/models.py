from django.db import models
import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length= 255)
    image = models.ImageField(upload_to= "media")
    body = models.TextField()

    def summary(self):
        return self.body[:100]
    def __str__(self):
        return self.title

