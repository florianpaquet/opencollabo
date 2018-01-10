from django import forms

from .models import (
    Person,
    Sentence)


class DenounceForm(forms.Form):

    person = forms.ModelChoiceField(
        Person.objects.all(),
        widget=forms.RadioSelect(),
        empty_label=None,
        required=True)

    sentence = forms.ModelChoiceField(
        Sentence.objects.all(),
        widget=forms.RadioSelect(),
        empty_label=None,
        required=True)

    def say(self):
        person = self.cleaned_data['person']
        sentence = self.cleaned_data['sentence']

        sentence.say(person)
