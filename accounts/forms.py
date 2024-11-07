from django import forms

class OTPLoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    otp_token = forms.CharField(max_length=6, label="OTP Token")
