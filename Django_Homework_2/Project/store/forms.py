# shop/forms.py

from django import forms
from .models import Product, Category, CustomUser
from django.contrib.auth.forms import UserCreationForm


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'date_of_birth', 'phone_number', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email
