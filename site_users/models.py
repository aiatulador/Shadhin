from django.db import models
from django.contrib.auth.models import User


class SiteUsers(models.Model):
    User_Name = models.TextField(primary_key=True, db_column='User Name')
    First_Name = models.CharField(max_length=30, db_column='First Name')
    Last_Name = models.CharField(max_length=30, db_column='Last Name')
    Email = models.EmailField(max_length=20, db_column='Email')
    Phone_Number = models.IntegerField(db_column='Phone Number')
    Password = models.CharField(db_column='Password', max_length=50)
    Profession = models.CharField(max_length=30, db_column='Profession')
    Age = models.IntegerField(db_column='Age')
    Address = models.CharField(max_length=100, db_column='Address')


class UserReg(models.Model):
    user_name = models.TextField(max_length=10)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=30)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=10, blank=True)
    about = models.CharField(max_length=150, blank=True)
    age = models.CharField(max_length=3, blank=True)
    profession = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=10, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_picture')

    def __str__(self):
        return str(self.user.first_name)

    def __str__(self):
        return str(self.user.last_name)

    def __str__(self):
        return str(self.user.email)

    def __str__(self):
        return str(self.user.profile.phone)

    def __str__(self):
        return str(self.user.profile.about)

    def __str__(self):
        return str(self.user.profile.age)

    def __str__(self):
        return str(self.user.profile.profession)

    def __str__(self):
        return str(self.user.profile.country)

    def __str__(self):
        return str(self.user.profile.address)

    def __str__(self):
        return str(self.user.profile.city)

    def __str__(self):
        return str(self.user.username)











