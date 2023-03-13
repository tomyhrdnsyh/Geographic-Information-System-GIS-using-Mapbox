from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.edit import CreateView
import pandas as pd
from collections import defaultdict
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

        wisata = Wisata.objects.values('nama_tempat', 'latitude', 'longitude', 'lokasi', 'galeri__gambar')
        wisata_dd = defaultdict(list)
        for item in wisata:
            wisata_dd[item['nama_tempat']].append(item['galeri__gambar'])
        print(wisata_dd)
        context['wisata'] = wisata
        return context