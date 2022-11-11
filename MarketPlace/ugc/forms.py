from django import forms
from .models import *


class AddMailingForm(forms.Form):
    email = forms.CharField(max_length=255)
