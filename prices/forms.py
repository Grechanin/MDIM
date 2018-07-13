from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import OrderModel

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = [
        	"order_name",
        	"client_name",
        	"phone_number",
        	"email",
        	"coment"
        ]
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            # 'phone_number': PhoneNumberPrefixWidget(),
        }
