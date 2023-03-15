from django.urls import path
from .views import *


urlpatterns = [
    path('', WisataView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
]