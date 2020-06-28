from django.urls import reverse
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


class definitionDetailView(DetailView):
    model = definition


class definitionUpdateView(UpdateView):
    model = definition
    form_class = definitionForm
