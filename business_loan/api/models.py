from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    family_members = models.IntegerField()

class BusinessDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    business_age = models.IntegerField()

class LoanApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(default="Pending", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
