from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    first_name = models.CharField(max_length=30, editable=True)
    last_name = models.CharField(max_length=150, editable=True)
    name = models.CharField(max_length=150)
    
    def __str__(self):
        print(f'{self.username} : {self.is_authenticated}')
        return f'{self.name}({self.username})'