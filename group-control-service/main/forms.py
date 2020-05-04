from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = StudyGroup
        fields = {'title', 'groupType', 'start', 'end'}
        widgets = {
            'start': DateInput(),
            'end': DateInput(),
        }

class JoinGroupForm(forms.ModelForm):
    class Meta:
        model = StudyGroup
        fields = {'code'}