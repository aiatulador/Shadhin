# Generated by Django 3.1.7 on 2021-03-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='Job_Code',
            field=models.IntegerField(db_column='Job Code', primary_key=True, serialize=False),
        ),
    ]
