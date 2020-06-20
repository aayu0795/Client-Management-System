from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


GENDER = {
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others')
}


class Customer(models.Model):
    agent = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER, max_length=1)
    contact = models.IntegerField()

    def __str__(self):
        return self.name
