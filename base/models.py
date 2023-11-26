from django.db import models

LOCATION_CHOICES = [
    ("BN", "Bonny Island"),
    ("OW", "Owerri"),
    ("OL", "Online"),
]


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    location = models.CharField(max_length=255, blank=False, choices=LOCATION_CHOICES, default='Undecided')
    payment_status = models.BooleanField(default=False)
    # location = models.CharField(max_length=255)
   
    def __str__(self):
        return self.first_name