from django.urls import path
from .views import WisataView, about


urlpatterns = [
    path('', WisataView.as_view(), name='home'),
    path('about/', about, name='about'),
]