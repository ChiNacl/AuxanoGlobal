from django.db import models

# Create your models here.
class Audio(models.Model):
    title = models.CharField(max_length=120)
    audio = models.FileField(upload_to='audio/', max_length=100)
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=192)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, default="08000000000")
    subject = models.CharField(max_length=192)
    

    def __str__(self):
        return self.name


class Partnership(models.Model):
    name = models.CharField(max_length=192)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, default="08000000000")  
    location = models.CharField(max_length=30, default="null")
    donation = models.IntegerField()

    def __str__(self):
        return self.name