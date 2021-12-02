from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .manager import UserProfileManger
# Create your models here.

class UserProfile(AbstractUser):
    username=models.CharField(_('username'),max_length=200,default='guest_user')
    email=models.EmailField(_('email address'),unique=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=UserProfileManger()

    def __str__(self):
        return self.email