from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.
admin.site.unregister(Group)


@admin.register(Wisata)
class WisataAdmin(admin.ModelAdmin):
    list_display = ("id_tempat", "nama_tempat", "latitude", "longitude", "lokasi",
                    "keterangan")


@admin.register(Galeri)
class GaleriAdmin(admin.ModelAdmin):
    list_display = ("id_galeri", "wisata", "nama_galeri", "gambar", "keterangan",)
