from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .manager import UserProfileManger
from multiselectfield import MultiSelectField
# Create your models here.

class LowercaseEmailField(models.EmailField):
    """
    Override EmailField to convert emails to lowercase before saving.
    """
    def to_python(self, value):
        """
        Convert email to lowercase.
        """
        value = super(LowercaseEmailField, self).to_python(value)
        # Value can be None so check that it's a string before lowercasing.
        if isinstance(value, str):
            return value.lower()
        return value


class Types(models.TextChoices):
    SELLER="S","Seller"
    CUSTOMER="C","Customer"

class UserProfile(AbstractUser):
    username=models.CharField(_('username'),max_length=200,default='guest_user')
    email=LowercaseEmailField(_('email address'),unique=True)
    type=MultiSelectField(choices=Types.choices,default=[],null=True,blank=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=UserProfileManger()

    default_type=Types.CUSTOMER

    def save(self,*args,**kwargs):
        if not self.id:             # So that it works only while Creation and not during Update
            self.type.append(self.default_type)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.email

