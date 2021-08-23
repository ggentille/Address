from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = ["name", "email", "phone", "mobile", "address", "city", "state", "zipcode",]