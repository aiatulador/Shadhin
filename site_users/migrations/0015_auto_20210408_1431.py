# Generated by Django 3.1.7 on 2021-04-08 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_users', '0014_auto_20210408_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreg',
            name='first_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='last_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='password',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='user_name',
            field=models.TextField(max_length=10),
        ),
    ]
