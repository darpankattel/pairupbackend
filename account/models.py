from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    def get_picture_path(self, filename):
        return f"profile_pictures/{self.user.id}/{filename}"
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    picture = models.ImageField(upload_to=get_picture_path, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=GENDER_CHOICES)
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-user__id']


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ['-profile__user__id', '-start_date']


class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['-profile__user__id', 'name']

class Connection(models.Model):
    profile1 = models.ForeignKey(Profile, related_name='connections_as_profile1', on_delete=models.CASCADE)
    profile2 = models.ForeignKey(Profile, related_name='connections_as_profile2', on_delete=models.CASCADE)
    date_connected = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_connected']

class ConnectionRequest(models.Model):
    profile1 = models.ForeignKey(Profile, related_name='requests_as_profile1', on_delete=models.CASCADE)
    profile2 = models.ForeignKey(Profile, related_name='requests_as_profile2', on_delete=models.CASCADE)
    date_requested = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_requested']


class Block(models.Model):
    profile1 = models.ForeignKey(Profile, related_name='blocks_as_profile1', on_delete=models.CASCADE)
    profile2 = models.ForeignKey(Profile, related_name='blocks_as_profile2', on_delete=models.CASCADE)
    date_blocked = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_blocked']
