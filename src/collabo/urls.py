from django.urls import path

from .views import (
    DenounceFormView,
    PersonCreateView,
    SentenceCreateView)


urlpatterns = [
    path('', DenounceFormView.as_view(), name='denounce'),
    path('add-person/', PersonCreateView.as_view(), name='add-person'),
    path('add-sentence/', SentenceCreateView.as_view(), name='add-sentence'),
]
