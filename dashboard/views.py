from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User, Group


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
        else:
            place["galeri__gambar"] = list(map(lambda x: '/' + x, place["galeri__gambar"]))
        output.append(place)

    return output


class WisataView(CreateView):
    model = Wisata
    fields = ['nama_tempat']
    template_name = 'maps.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        center = [110.96072044262617, -7.342371509127405]
        zoom = 7

        if self.request.GET:
            search = self.request.GET.get('search_address')
            filter_category = self.request.GET.get('category')

            if filter_category:
                if filter_category == 'all':
                    wisata = Wisata.objects.values('nama_tempat', 'latitude', 'longitude', 'lokasi', 'galeri__gambar')

                else:
                    wisata = Wisata.objects.filter(jenis=filter_category).values('nama_tempat', 'latitude', 'longitude', 'lokasi', 'galeri__gambar')

            if search:
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
        context['mapbox_access_token'] = 'pk.eyJ1Ijoicm9uaWFydGFzaXRpbmphayIsImEiOiJja2pzZGdkZTkxNnpjMnRwNXY4MmJwdTJuIn0.yy8btAs8q76jGtbiZY628w '
        context['center'] = center
        context['zoom'] = zoom
        return context


def home(request):
    context = {}
    return render(request, 'index.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


def register(request):
    context = {}

    if request.POST:

        # DATA PARSING
        data = request.POST
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        # create a new user object
        new_user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email)

        # change status user to staff
        new_user.is_staff = True

        # save the user to the database
        new_user.save()

        add_to_group = Group.objects.get(name='Pengunjung')
        add_to_group.user_set.add(new_user)

        context['message'] = f'Selamat, {username} berhasil didaftar'

    return render(request, 'register.html', context)
