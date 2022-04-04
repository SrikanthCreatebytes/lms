from django.contrib.auth.models import User
from django.db import models
import uuid

ROLES = (
    ("user", "USER"),
    ("admin", "ADMIN"),

)


class UserProfile(models.Model):
    """ users can create their own profiles """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True, unique=True)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    user_role = models.CharField(max_length=200, choices=ROLES)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.email if self.email else self.phone_number)





