from django.urls import path
from .views import WisataView


urlpatterns = [
    path('', WisataView.as_view(), name='home'),
]