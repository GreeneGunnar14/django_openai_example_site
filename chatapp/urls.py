from .views import index, docs, linksview
from django.urls import path

urlpatterns = [
  path('', index, name='Home'),
  path('docs', docs, name='Documentation'),
  path('links', linksview, name='Links')
]