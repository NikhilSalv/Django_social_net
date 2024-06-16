from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(blank=False)
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_images', default='default.png')
    location = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username