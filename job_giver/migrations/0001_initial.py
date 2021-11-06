# Generated by Django 3.1.7 on 2021-03-27 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('site_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobGiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_column='Name')),
                ('Mail', models.CharField(max_length=100)),
                ('Phone_Number', models.IntegerField()),
                ('User_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_users.siteusers')),
            ],
        ),
    ]
