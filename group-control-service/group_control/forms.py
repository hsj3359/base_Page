from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = {'title', 'date', 'time', 'content'}
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }

class NoticeForm(forms.ModelForm):

    class Meta:
        model = Notice
        fields = {'title', 'type', 'content'}

class PostForm(forms.ModelForm):
    # title = forms.CharField()
    # content = forms.CharField()
    # file = forms.FileField(required=False)

    class Meta:
        model = Post
        fields = {'title', 'content', 'file'}


