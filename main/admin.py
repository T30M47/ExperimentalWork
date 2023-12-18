from django.contrib import admin
from .models import *
# Register your models here.
modeli = [Proizvod_SIndeksom, Proizvod_bezIndeksa, Proizvod_DioIndeksa, Proizvod_KriviIndeks, Proizvod_bezIndeksa_MaloRedaka, Proizvod_SIndeksom_MaloRedaka, Proizvod_SIndeksom_VelikaKard, Proizvod_DioIndeksa_VelikaKard, Proizvod_KriviIndeks_VelikaKard, Proizvod_SIndeksom_Datum, Proizvod_SIndeksom_VelikaKard_Datum]

admin.site.register(modeli)