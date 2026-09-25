from django import forms
from .models import Topic, entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        label = {'text': ''}
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = entry
        fields = ['topic', 'text']
        labels = {'text': ''}
