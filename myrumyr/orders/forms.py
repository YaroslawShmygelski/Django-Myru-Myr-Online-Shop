from django import forms
from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'city']
        labels =['First Name', 'Last Name', 'Email', 'Phone Number', 'City']