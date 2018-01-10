from django.urls import reverse_lazy
from django.views.generic import (
    FormView,
    CreateView)

from .forms import DenounceForm
from .models import (
    Person,
    Sentence)


class DenounceFormView(FormView):

    form_class = DenounceForm
    template_name = 'collabo/denounce.html'
    success_url = reverse_lazy('denounce')

    def form_valid(self, form):
        form.say()
        return super().form_valid(form)


class PersonCreateView(CreateView):

    model = Person
    fields = ('name',)
    success_url = reverse_lazy('denounce')


class SentenceCreateView(CreateView):

    model = Sentence
    fields = ('text',)
    success_url = reverse_lazy('denounce')
