# users/forms.py
from django import forms
from allauth.account.forms import SignupForm
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomSignupForm(SignupForm):
    mobile_number = forms.CharField(max_length=15, required=True)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.mobile_number = self.cleaned_data['mobile_number']
        user.save()
        return user

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'mobile_number')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'mobile_number')
