from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    skills = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField(max_length=254, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50)
    link = models.TextField(max_length=500, blank=True)