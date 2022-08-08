
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):

    first_name = forms.CharField(max_length=50) # Required
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'password1','password2']

        def clean_email(self):
            email = self.cleaned_data['username']

            correct_email = "@tru.ca"

            if correct_email not in email:
                raise forms.ValidationError("Please enter TRU email")

            return email

        
