from django import forms
from .models import *


class AddMailingForm(forms.Form):
    # email = forms.EmailField(max_length=255)
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    class Meta:
        model = EmailForMailing
        fields = ['email']

