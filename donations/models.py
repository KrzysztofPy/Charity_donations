from django.db import models
from django.contrib.auth.models import User



INSTITUTION_CHOICES = [
    (1, "fundacja"),
    (2, "organizacja pozarządowa"),
    (3, "zbiórka lokalna")
]


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    type = models.IntegerField(choices=INSTITUTION_CHOICES, default=1)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ["type"]

    def __str__(self):
        return f"Institution: {INSTITUTION_CHOICES[self.type]} {self.name}"
    

class Donation(models.Model):
    quantity = models.IntegerField() #liczba workow
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=512) #ulica + numer domu
    phone_number = models.CharField(max_length=24) #numer telefonu jako string
    city = models.CharField(max_length=24)
    zip_code = models.CharField(max_length=24)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Donation of {self.quantity} of {self.categories} from {self.institution}"

