from django.db import models
from django.utils.timezone import now
from django.utils import timezone
# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=60)
    father_name = models.CharField(max_length=60)
    cnic = models.CharField(max_length=60)
    designation = models.CharField(max_length=60)
    district = models.CharField(max_length=60)
    mobile = models.CharField(max_length=60)
    imei = models.CharField(max_length=60)
    joining_date = models.CharField(max_length=60)
    # date = models.DateTimeField(default=timezone.now, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.cnic

class attendance(models.Model):
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    cnic = models.CharField(max_length=60)
    imei = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    lat = models.CharField(max_length=60)
    long = models.CharField(max_length=60)
    type = models.CharField(max_length=60)
    date1 = models.CharField(max_length=60)

    def __str__(self):
        return self.cnic

class geolog(models.Model):
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    cnic = models.CharField(max_length=60)
    imei = models.CharField(max_length=60)
    lat = models.CharField(max_length=60)
    long = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    date1 = models.CharField(max_length=60)

    def __str__(self):
        return self.cnic
