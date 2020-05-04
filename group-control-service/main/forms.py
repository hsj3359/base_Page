from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = {'title', 'groupType', 'start', 'end'}
        widgets = {
            'start': DateInput(),
            'end': DateInput(),
        }

class JoinForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = {'code'}