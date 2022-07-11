from django.db import models

# Create your models here.
class Audio(models.Model):
    title = models.CharField(max_length=120)
    audio = models.FileField(upload_to='audio/', max_length=100)
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=192)
    phone_number = models.CharField(max_length=12, default="08000000000")
    email = models.EmailField()
    subject = models.CharField(max_length=192)
    message = models.TextField()

    def __str__(self):
        return self.name


class Partnership(models.Model):
    name = models.CharField(max_length=192)
    phone_number = models.CharField(max_length=12, default="08000000000")
    email = models.EmailField()
    location = models.CharField(max_length=30, default="null")
    donation = models.IntegerField()

    def __str__(self):
        return self.name