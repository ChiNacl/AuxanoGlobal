from django.forms import ModelForm
from .models import Contact, Partnership

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class PartnershipForm(ModelForm):
    class Meta:
        model = Partnership
        fields = '__all__'