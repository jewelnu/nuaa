from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  # Set email as the unique identifier
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email