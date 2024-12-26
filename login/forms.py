from django import forms
from login.models import User

professions = [(1, 'Student'), (2, 'Educator (Teacher/Professor)'), (3, 'Engineer/Technician'), (4, 'Healthcare Professional'), (5, 'Corporate/Office Worker'), (6, 'Service Industry (Retail/Hospitality)'), (7, 'Agriculture/Fisheries'), (8, 'Self-Employed'), (9, 'Other')]
purpose = [(1, 'Personal'), (2, 'Research/Academic Purposes'), (3, 'Business/Commercial'), (4, 'Other')]

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    password = forms.CharField(widget = forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'profession', 'purpose_of_joining', 'username', 'password']
    password = forms.CharField(widget = forms.PasswordInput)