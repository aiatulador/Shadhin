from django.db import models

from site_users.models import Profile


class PostWork(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, db_column="User")
    Company_Name = models.CharField(max_length=50, db_column="Company Name")
    Title = models.CharField(max_length=50, db_column="Title")
    Work_Type = models.CharField(max_length=50, db_column="Work Type")
    Description = models.CharField(max_length=100, db_column="Description")
    Requirements = models.CharField(max_length=100, db_column="Requirements")
    Experience = models.CharField(max_length=500, db_column="Experience")
    Salary = models.IntegerField(db_column="Salary")
    Location = models.CharField(max_length=100, db_column="Location")
    Vacancy = models.CharField(max_length=10, db_column="Vacancy")
