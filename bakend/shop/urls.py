from django.urls import path
from .views import one

urlpatterns = [
    path('',one.as_view(),name='home')
]
