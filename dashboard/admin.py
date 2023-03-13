from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.
admin.site.unregister(Group)


class GaleriWisataInline(admin.TabularInline):
    model = Galeri
    extra = 0


@admin.register(Wisata)
class WisataAdmin(admin.ModelAdmin):
    inlines = [GaleriWisataInline]
    list_display = ("id_tempat", "nama_tempat", "latitude", "longitude", "lokasi",
                    "keterangan")

# @admin.register(Galeri)
# class GaleriAdmin(admin.ModelAdmin):
#     list_display = ("id_galeri", "wisata", "nama_galeri", "gambar", "keterangan",)
