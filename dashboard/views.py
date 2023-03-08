from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *

# Create your views here.


class WisataView(CreateView):

    model = Wisata
    fields = ['nama_tempat']
    template_name = 'index.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1Ijoicm9uaWFydGFzaXRpbmphayIsImEiOiJja2pzZGdkZTkxNnpjMnRwNXY4MmJwdTJuIn0.yy8btAs8q76jGtbiZY628w '
        context['wisata'] = Wisata.objects.all()
        return context