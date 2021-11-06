from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from .models import Profile, UserReg
from post_work.models import PostWork


class UseRegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  ]


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class UserJobSetForm(forms.ModelForm):
    Company_Name = forms.CharField()
    Title = forms.CharField()
    Work_Type = forms.CharField()
    Description = forms.CharField()
    Requirements = forms.CharField()
    Experience = forms.CharField(required=False)
    Salary = forms.IntegerField()
    Location = forms.CharField(required=False)
    Vacancy = forms.CharField(required=False)

    class Meta:
        model = PostWork
        fields = [
            'Company_Name',
            'Title',
            'Work_Type',
            'Description',
            'Requirements',
            'Experience',
            'Salary',
            'Location',
            'Vacancy',
            'user',
        ]


class ProfileUpdateFrom(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = [
            'about',
            'age',
            'profession',
            'address',
            'city',
            'country',
            'phone',
            'profile_picture',
        ]
