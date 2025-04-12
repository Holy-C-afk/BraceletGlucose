from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),
    )
    
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='patient')
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    emergency_contact = models.CharField(max_length=100, blank=True)
    emergency_phone = models.CharField(max_length=15, blank=True)
    
    # Medical information
    blood_type = models.CharField(max_length=5, blank=True)
    allergies = models.TextField(blank=True)
    medications = models.TextField(blank=True)
    
    # Doctor specific fields
    specialization = models.CharField(max_length=100, blank=True)
    license_number = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_user_type_display()})"
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users' 