from django.db import models


class Jobs(models.Model):
    Job_Name = models.TextField(db_column='Job Name')
    Job_Type = models.CharField(max_length=50, db_column='Job Type')
    Job_Code = models.IntegerField(primary_key=True, db_column='Job Code')
    Salary = models.CharField(max_length=10, db_column='Salary')
    Requirements = models.TextField(db_column='Requirements')
    Experience = models.TextField(db_column='Experience')


