from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class AccessGrantTable(models.Model):
    
    granted_by = models.CharField(max_length=64)
    user = models.CharField(max_length=64)
    given_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    reason = models.TextField()
    inventory  = models.TextField()
    user_or_group_identifier = models.CharField(max_length=64)
    is_active = models.BooleanField(default = True)
    
    
    def __str__(self):
    
        return self.user
    
    
