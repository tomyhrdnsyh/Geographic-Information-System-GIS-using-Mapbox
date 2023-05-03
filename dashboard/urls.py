from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('maps/', WisataView.as_view(), name='maps'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
]