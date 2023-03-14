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

        output = []
        places = {}

        for item in wisata:
            name = item["nama_tempat"]
            if name in places:
                places[name]["galeri__gambar"].append(item["galeri__gambar"])
            else:
                places[name] = item
                places[name]["galeri__gambar"] = [item["galeri__gambar"]]

        for place in places.values():
            if place["galeri__gambar"][0] is None and len(place["galeri__gambar"]) == 1:
                place["galeri__gambar"] = ['static/ing/logo 2.png']
            output.append(place)

        context['wisata'] = output
        return context