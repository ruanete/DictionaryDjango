from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import TextField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class term(models.Model):

    # Fields
    word = models.CharField(max_length=100, unique=True, verbose_name='Termino')


    class Meta:
        ordering = ('-word',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('dictionary_django_term_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('dictionary_django_term_update', args=(self.pk,))

    def __str__(self):
        return self.word


class definition(models.Model):

    # Fields
    meaning = models.TextField(max_length=200, verbose_name='Significado')

    # Relationship Fields
    word_meaning_relationship = models.ForeignKey(
        'dictionary_django.term',
        on_delete=models.CASCADE, related_name="definitions", verbose_name='Termino'
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('dictionary_django_definition_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('dictionary_django_definition_update', args=(self.pk,))


