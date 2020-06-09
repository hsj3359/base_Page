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

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = {'title', 'subject', 'content'}

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = {'title'}

class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = {'message', 'photo'}

class PostForm(forms.ModelForm):
    title = forms.CharField(label='')
    widget = forms.Textarea(attrs={
        'row': '5',
        'cols': '50',
        'placeholder': '140자까지 입력 가능합니다.'
    })
    content = forms.CharField(label='', widget=widget)
    subject = forms.CharField(label='')
    photo = forms.ImageField(label='', required=False)

    class Meta:
        model = Post
        fields = {'title', 'content', 'subject', 'photo'}


