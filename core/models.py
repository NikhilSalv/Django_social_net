from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(primary_key=True,blank=False)
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_images', default='default.png')
    location = models.CharField(max_length=50, blank=True, default="Dublin")

    def __str__(self):
        return self.user.username