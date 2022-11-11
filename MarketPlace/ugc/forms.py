from django import forms
from .models import *


class AddMailingForm(forms.Form):
    email = forms.EmailField(max_length=255)
