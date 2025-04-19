
from django.db import models

class Comic(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='comics/')

    def __str__(self):
        return self.title
    

# Create your models here.
