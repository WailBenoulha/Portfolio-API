from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager



class User(AbstractUser):
    cv = models.FileField(upload_to='files/',null=True,blank=True)
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Skill(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skills/')

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='projects/')
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title

class Experience(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    finish_date = models.DateField()

    def __str__(self):
        return self.name
    
class Education(models.Model):
    univ = models.CharField(max_length=255)
    start_date = models.DateField()
    finish_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'{self.univ}-{self.start_date}-{self.finish_date}'