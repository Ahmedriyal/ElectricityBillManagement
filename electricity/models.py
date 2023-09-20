from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class occupants(models.Model):
    occupant_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.occupant_name


class floors(models.Model):
    floor_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.floor_name


class locations(models.Model):
    A = 'A'
    B = 'B'
    C = 'C'
    C1 = 'C1'
    C2 = 'C2'

    unit_choices = [
        (A, 'A'),
        (B, 'B'),
        (C, 'C'),
        (C1, 'C1'),
        (C2, 'C2')
    ]
    occupant_id = models.ForeignKey(occupants, on_delete=models.SET_NULL, null=True, blank=True)
    floor_id = models.ForeignKey(floors, on_delete=models.SET_NULL, null=True, blank=True)
    unit = models.CharField(max_length=50, choices=unit_choices, null=True, blank=True)

class electricities(models.Model):
    date = models.DateField()
    occupant_id = models.ForeignKey(occupants, on_delete=models.SET_NULL, null=True, blank=True)
    dpdc1 = models.CharField(max_length=200, null=True, blank=True)
    dpdc2 = models.CharField(max_length=200, null=True, blank=True)
    dpdc3 = models.CharField(max_length=200, null=True, blank=True)
    generator1 = models.CharField(max_length=200, null=True, blank=True)
    generator2 = models.CharField(max_length=200, null=True, blank=True)
    generator3 = models.CharField(max_length=200, null=True, blank=True)


    