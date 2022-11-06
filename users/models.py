from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    user_image = models.ImageField(upload_to='users/')
    phone = models.CharField(max_length=13)
    instagram_url = models.URLField()
    telegram_url = models.URLField()
    site_url = models.URLField()
