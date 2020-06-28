from django.contrib import admin
from django import forms
from .models import term, definition

class termAdminForm(forms.ModelForm):

    class Meta:
        model = term
        fields = '__all__'


class termAdmin(admin.ModelAdmin):
    form = termAdminForm
    list_display = ['word']
    readonly_fields = ['word']

admin.site.register(term, termAdmin)


class definitionAdminForm(forms.ModelForm):

    class Meta:
        model = definition
        fields = '__all__'


class definitionAdmin(admin.ModelAdmin):
    form = definitionAdminForm
    list_display = ['meaning']
    readonly_fields = ['meaning']

admin.site.register(definition, definitionAdmin)


