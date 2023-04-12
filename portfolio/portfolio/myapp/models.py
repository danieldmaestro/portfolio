from django.db import models


# Create your models here.
# Define the models for the database

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='project_media/')

    def __str__(self):
        return self.title

class Dev(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=120)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()

    def __str__(self):
        return self.name

class Stack(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Visitor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name