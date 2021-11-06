from django.db import models
from site_users.models import SiteUsers


class JobSeeker(models.Model):
    name = models.TextField(db_column='Name')

    Mail = models.CharField(max_length=100)
    Phone_Number = models.IntegerField()
    User_Name = models.ForeignKey(SiteUsers, on_delete=models.CASCADE)
