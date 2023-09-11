from .views import index, docs
from django.urls import path

urlpatterns = [
  path('', index, name='Home'),
  path('docs', docs, name='Documentation')
]