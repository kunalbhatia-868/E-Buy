from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .manager import UserProfileManger
# Create your models here.

class UserProfile(AbstractUser):
    username=None
    email=models.EmailField(_('email address'),unique=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=UserProfileManger()

    def __str__(self):
        return self.email