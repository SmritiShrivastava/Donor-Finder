from django.db import models
from django.contrib.auth.models import User

blood_groups = (
    ("A+", "A+"),
    ("A-", "A-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("O+", "O+"),
    ("O-", "O-")
)

Gender_choices = (
    ("Male","Male"),
    ("Female","Female"),
    ("others","others")
)

# Create your models here.
class userProfiles(User):
    firstName = models.CharField(max_length = 200)
    lastName = models.CharField(max_length = 200)
    bloodGroup = models.CharField(max_length=50, choices=blood_groups)
    gender = models.CharField(max_length=50, choices=Gender_choices)
    age = models.IntegerField()
    contactNumber = models.IntegerField()
    created = models.DateTimeField(auto_now = True)

class donorModel(models.Model):
    donated = models.BooleanField(default = False)
    drinked = models.BooleanField(default = False)
    disease = models.BooleanField(default = False)
    userkey = models.ForeignKey(userProfiles, on_delete = models.CASCADE)
    bloodGroup = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.userkey.username