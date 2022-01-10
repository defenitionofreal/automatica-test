from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    """ Custom User Model """

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Worker(models.Model):
    """ Worker model """
    name = models.CharField(max_length=100)
    phone = PhoneNumberField(unique=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    """ A store model """
    worker = models.OneToOneField(Worker, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Visit(models.Model):
    """ Visit model """
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.store} at {self.date}'
