from django import forms

from dashboard import models


class QuestionForm(forms.ModelForm):
    question = forms.CharField(label="Vraag")
    answer = forms.CharField(label="Antwoord", widget=forms.Textarea())
    keywords = forms.CharField(label="Tags (1 per lijn)", widget=forms.Textarea(
        attrs={'placeholder': 'tag1\ntag2\ntag3'}
    ))

    class Meta:
        model = models.Question
        fields = ['question', 'answer', 'keywords']


class ChannelForm(forms.ModelForm):
    channel_id = forms.CharField(label="Kanaal ID")

    class Meta:
        model = models.GuildChannel
        fields = ['channel_id']
