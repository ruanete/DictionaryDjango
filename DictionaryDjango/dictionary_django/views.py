from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from .models import term, definition
from .forms import termForm, definitionForm


class termListView(ListView):
    model = term


class termCreateView(CreateView):
    model = term
    form_class = termForm


class termRemoveView(DeleteView):
    model = term
    success_url = "/dictionary_django/dictionary_django/term/"


class termDetailView(DetailView):
    model = term


class termUpdateView(UpdateView):
    model = term
    form_class = termForm


class definitionListView(ListView):
    model = definition


class definitionCreateView(CreateView):
    model = definition
    form_class = definitionForm


class definitionRemoveView(DeleteView):
    model = definition
    success_url = "/dictionary_django/dictionary_django/definition/"


class definitionDetailView(DetailView):
    model = definition


class definitionUpdateView(UpdateView):
    model = definition
    form_class = definitionForm

