from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import uuid


class CustomUser(AbstractUser):
    pass

groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_set", # A unique related_name is often required
        related_query_name="customuser",
    )

user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set", # A unique related_name is often required
        related_query_name="customuser",
    )

class Party(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    party_date = models.DateField()
    party_time = models.TimeField()
    invitation = models.TextField()
    venue = models.CharField(max_length=200)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="organized_parties")

    class Meta:
        verbose_name_plural = "parties"

    def __str__(self):
        return f"{self.venue}, {self.party_date}"


class Gift(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    gift = models.CharField(max_length=200)
    price = models.FloatField(blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

    def __str__(self):
        return self.gift


class Guest(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    attending = models.BooleanField(default=False)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name="guests")

    def __str__(self):
        return str(self.name)
    
    class Meta:
     verbose_name = 'Custom User'
     verbose_name_plural = 'Custom Users'

     def __str__(self):
        return self.username
