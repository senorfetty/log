from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Customer(AbstractUser):
    phone_number = models.CharField(max_length=15)
    loyalty_points = models.IntegerField(default=0)
    groups = models.ManyToManyField(Group, related_name='customer_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customer_set', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

class Mkubwa(AbstractUser):
    is_admin = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group, related_name='admin_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='admin_set', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Mkubwa'
        verbose_name_plural = 'Wakubwa'
