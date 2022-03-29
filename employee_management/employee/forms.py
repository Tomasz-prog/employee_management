from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models  import Employee

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class AddEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = [
            'usercode',
            'first_name',
            'last_name',
            'team_leader',
            'supervisor',
            'shift',
            'start_work',
            'dept',
        ]


