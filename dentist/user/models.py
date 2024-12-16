from django.db import models # type: ignore

# Create your models here.

from django.contrib.auth.models import AbstractUser # type: ignore
from django.db import models # type: ignore

class User(AbstractUser): 
    
    ROLE_CHOICES = [ ('admin', 'Admin'), 
                    ('dentist', 'Dentist'), 
                    ('receptionist', 'Receptionist'), 
                    ('patient', 'Patient'), ] 
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES) 
    
    phone = models.CharField(max_length=15, blank=True, null=True) 