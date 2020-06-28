from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'term', api.termViewSet)
router.register(r'definition', api.definitionViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for term
    path('dictionary_django/term/', views.termListView.as_view(template_name = "term/index.html"), name='dictionary_django_term_list'),
    path('dictionary_django/term/create/', views.termCreateView.as_view(template_name = "term/create.html"), name='dictionary_django_term_create'),
    path('dictionary_django/term/remove/<int:pk>/', views.termRemoveView.as_view(), name='dictionary_django_term_remove'),
    path('dictionary_django/term/detail/<int:pk>/', views.termDetailView.as_view(template_name = "term/details.html"), name='dictionary_django_term_detail'),
    path('dictionary_django/term/update/<int:pk>/', views.termUpdateView.as_view(template_name = "term/update.html"), name='dictionary_django_term_update'),
)

urlpatterns += (
    # urls for definition
    path('dictionary_django/definition/', views.definitionListView.as_view(template_name = "definition/index.html"), name='dictionary_django_definition_list'),
    path('dictionary_django/definition/create/', views.definitionCreateView.as_view(template_name = "definition/create.html"), name='dictionary_django_definition_create'),
    path('dictionary_django/definition/remove/<int:pk>/', views.definitionRemoveView.as_view(), name='dictionary_django_term_remove'),
    path('dictionary_django/definition/detail/<int:pk>/', views.definitionDetailView.as_view(template_name = "definition/details.html"), name='dictionary_django_definition_detail'),
    path('dictionary_django/definition/update/<int:pk>/', views.definitionUpdateView.as_view(template_name = "definition/update.html"), name='dictionary_django_definition_update'),
)

