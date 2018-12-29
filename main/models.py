from django.db import models

# Create your models here.

class Corp(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=32)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return(self.name)

class Preview(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='galery/',max_length=255)

    def __str__(self):
        return(self.title)

class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    content = models.TextField(max_length=10000)
    preview = models.ForeignKey(Preview, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return(self.title)
        