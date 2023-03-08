from django.db import models


# Create your models here.
class Wisata(models.Model):
    id_tempat = models.AutoField(primary_key=True)
    nama_tempat = models.CharField(max_length=200)
    latitude = models.FloatField(max_length=200)
    longitude = models.FloatField(max_length=200)
    lokasi = models.CharField(max_length=200)
    keterangan = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nama_tempat

    class Meta:
        verbose_name_plural = 'Wisata'


class Galeri(models.Model):
    id_galeri = models.AutoField(primary_key=True)
    wisata = models.ForeignKey(Wisata, on_delete=models.CASCADE)
    nama_galeri = models.CharField(max_length=250)
    gambar = models.ImageField(upload_to='dashboard/image_upload', null=True)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama_galeri

    class Meta:
        verbose_name_plural = 'Galeri'