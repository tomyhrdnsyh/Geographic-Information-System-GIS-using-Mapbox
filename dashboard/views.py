from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *
from django.db.models import Q


# Create your views here.
def preprocess_output(wisata, request):
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
            place["galeri__gambar"] = [request.build_absolute_uri('/static/img/logo 2.png')]
        output.append(place)

    return output


class WisataView(CreateView):
    model = Wisata
    fields = ['nama_tempat']
    template_name = 'index.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        center = [110.96072044262617, -7.342371509127405]
        zoom = 7

        if self.request.GET:
            search = self.request.GET.get('search_address')

            wisata = Wisata.objects.filter(Q(nama_tempat__icontains=search) |
                                           Q(lokasi__icontains=search)).values('nama_tempat', 'latitude',
                                                                               'longitude', 'lokasi', 'galeri__gambar')

            if wisata:
                center = [wisata[0]['longitude'], wisata[0]['latitude']]
                zoom = 9

        else:
            wisata = Wisata.objects.values('nama_tempat', 'latitude', 'longitude', 'lokasi', 'galeri__gambar')

        # reprocess response wisata
        output = preprocess_output(wisata, self.request)

        # send to view
        context['wisata'] = output
        context[
            'mapbox_access_token'] = 'pk.eyJ1Ijoicm9uaWFydGFzaXRpbmphayIsImEiOiJja2pzZGdkZTkxNnpjMnRwNXY4MmJwdTJuIn0.yy8btAs8q76jGtbiZY628w '
        context['center'] = center
        context['zoom'] = zoom
        return context


def about(request):
    context = {}
    return render(request, 'about.html', context)
