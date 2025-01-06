from django import forms
from .models import Employee_profile

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Employee_profile
        fields = ['date_of_birth', 'phone_number', 'address']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}) 
            }
