from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import *
import time
from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from django.core.cache import cache
# Create your views here.

def homepage(request):
    return render(request, 'template.html')

class GetDataWithoutIndex(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        datum_kreiranja = request.GET.get('datum_kreiranja', '')

        proizvodi = Proizvod_bezIndeksa.objects.filter(
            naziv = naziv,
            cijena = cijena,
            datum_kreiranja = datum_kreiranja
        )

        proizvodi_json = list(proizvodi.values())
        cache_key = 'cache_key_for_GetDataWithoutIndex'
        cache.delete(cache_key)
        return JsonResponse(proizvodi_json, safe=False)

class GetDataWithIndex(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        datum_kreiranja = request.GET.get('datum_kreiranja', '')

        proizvodi = Proizvod_SIndeksom.objects.filter(
            naziv = naziv,
            cijena = cijena,
            datum_kreiranja = datum_kreiranja
        )

        proizvodi_json = list(proizvodi.values())
        cache_key = 'cache_key_for_GetDataWithIndex'
        cache.delete(cache_key)
        return JsonResponse(proizvodi_json, safe=False)

class GetDataWithPartIndex(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        datum_kreiranja = request.GET.get('datum_kreiranja', '')

        proizvodi = Proizvod_DioIndeksa.objects.filter(
            naziv = naziv,
            cijena = cijena,
            datum_kreiranja = datum_kreiranja
        )

        proizvodi_json = list(proizvodi.values())
        cache_key = 'cache_key_for_GetDataWithPartIndex'
        cache.delete(cache_key)
        return JsonResponse(proizvodi_json, safe=False)

class GetDataWithWrongIndex(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        
        proizvodi = Proizvod_KriviIndeks.objects.filter(
            naziv = naziv,
            cijena = cijena,
        )

        proizvodi_json = list(proizvodi.values())
        cache_key = 'cache_key_for_GetDataWithWrongIndex'
        cache.delete(cache_key)
        return JsonResponse(proizvodi_json, safe=False)


class GetDataWithoutIndexLessRows(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        datum_kreiranja = request.GET.get('datum_kreiranja', '')

        proizvodi = Proizvod_bezIndeksa_MaloRedaka.objects.filter(
            naziv = naziv,
            cijena = cijena,
            datum_kreiranja = datum_kreiranja
        )

        proizvodi_json = list(proizvodi.values())
        cache_key = 'cache_key_for_GetDataWithoutIndexLessRows'
        cache.delete(cache_key)
        return JsonResponse(proizvodi_json, safe=False)

class GetDataWithIndexLessRows(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        datum_kreiranja = request.GET.get('datum_kreiranja', '')

        proizvodi = Proizvod_SIndeksom_MaloRedaka.objects.filter(
            naziv = naziv,
            cijena = cijena,
            datum_kreiranja = datum_kreiranja
        )

        proizvodi_json = list(proizvodi.values())
        cache_key = 'cache_key_for_GetDataWithIndexLessRows'
        cache.delete(cache_key)
        return JsonResponse(proizvodi_json, safe=False)

class GetDataWithIndexBigCard(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        datum_kreiranja = request.GET.get('datum_kreiranja', '')

        proizvodi = Proizvod_SIndeksom_VelikaKard.objects.filter(
            naziv = naziv,
            cijena = cijena,
            datum_kreiranja = datum_kreiranja
        )

        proizvodi_json = list(proizvodi.values())
        cache_key = 'cache_key_for_GetDataWithIndexBigCard'
        cache.delete(cache_key)
        return JsonResponse(proizvodi_json, safe=False)

class GetDataWithPartIndexBigCard(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        datum_kreiranja = request.GET.get('datum_kreiranja', '')

        proizvodi = Proizvod_DioIndeksa_VelikaKard.objects.filter(
            naziv = naziv,
            cijena = cijena,
            datum_kreiranja = datum_kreiranja
        )

        proizvodi_json = list(proizvodi.values())
        cache_key = 'cache_key_for_GetDataWithPartIndexBigCard'
        cache.delete(cache_key)
        return JsonResponse(proizvodi_json, safe=False)

class GetDataWithWrongIndexBigCard(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        
        proizvodi = Proizvod_KriviIndeks_VelikaKard.objects.filter(
            naziv = naziv,
            cijena = cijena,
        )

        proizvodi_json = list(proizvodi.values())
        cache_key = 'cache_key_for_GetDataWithWrongIndexBigCard'
        cache.delete(cache_key)
        return JsonResponse(proizvodi_json, safe=False)

class GetDataWithIndexDate(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        
        proizvodi = Proizvod_SIndeksom_Datum.objects.filter(
            naziv = naziv,
            cijena = cijena,
        )

        proizvodi_json = list(proizvodi.values())
        cache_key = 'cache_key_for_GetDataWithIndexDate'
        cache.delete(cache_key)
        return JsonResponse(proizvodi_json, safe=False)

class GetDataWithIndexBigDate(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        
        proizvodi = Proizvod_SIndeksom_VelikaKard_Datum.objects.filter(
            naziv = naziv,
            cijena = cijena,
        )

        proizvodi_json = list(proizvodi.values())
        cache_key = 'cache_key_for_GetDataWithIndexBigDate'
        cache.delete(cache_key)
        return JsonResponse(proizvodi_json, safe=False)

class GetDataWithWrongIndexFull(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        datum_kreiranja = request.GET.get('datum_kreiranja', '')

        proizvodi = Proizvod_KriviIndeks.objects.filter(
            naziv = naziv,
            cijena = cijena,
            datum_kreiranja = datum_kreiranja
        )

        proizvodi_json = list(proizvodi.values())
        cache_key = 'cache_key_for_GetDataWithWrongIndexFull'
        cache.delete(cache_key)
        return JsonResponse(proizvodi_json, safe=False)

class GetDataWithWrongIndexBigCardFull(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        datum_kreiranja = request.GET.get('datum_kreiranja', '')

        proizvodi = Proizvod_KriviIndeks_VelikaKard.objects.filter(
            naziv = naziv,
            cijena = cijena,
            datum_kreiranja = datum_kreiranja
        )

        proizvodi_json = list(proizvodi.values())
        cache_key = 'cache_key_for_GetDataWithWrongIndexBigCardFull'
        cache.delete(cache_key)
        return JsonResponse(proizvodi_json, safe=False)


def testWithoutIndex(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    datum_kreiranja = request.GET.get('datum_kreiranja', '')
    
    url = f"http://localhost:8000/withoutIndex/?naziv={naziv}&cijena={cijena}&datum_kreiranja={datum_kreiranja}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena,
            'datum_kreiranja': datum_kreiranja,
        },
        'output': output,
    }
    
    cache_key = 'cache_key_for_GetDataWithoutIndex'
    cache.delete(cache_key)

    return JsonResponse(response_data)

def testWithIndex(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    datum_kreiranja = request.GET.get('datum_kreiranja', '')
    
    url = f"http://localhost:8000/withIndex/?naziv={naziv}&cijena={cijena}&datum_kreiranja={datum_kreiranja}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena,
            'datum_kreiranja': datum_kreiranja,
        },
        'output': output,
    }
    
    cache_key = 'cache_key_for_GetDataWithIndex'
    cache.delete(cache_key)

    return JsonResponse(response_data)

def testWithPartIndex(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    datum_kreiranja = request.GET.get('datum_kreiranja', '')
    
    url = f"http://localhost:8000/withPartIndex/?naziv={naziv}&cijena={cijena}&datum_kreiranja={datum_kreiranja}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena,
            'datum_kreiranja': datum_kreiranja,
        },
        'output': output,
    }
    
    cache_key = 'cache_key_for_GetDataWithPartIndex'
    cache.delete(cache_key)

    return JsonResponse(response_data)

def testWithWrongIndex(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    
    url = f"http://localhost:8000/withWrongIndex/?naziv={naziv}&cijena={cijena}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena
        },
        'output': output,
    }
    
    cache_key = 'cache_key_for_GetDataWithWrongIndex'
    cache.delete(cache_key)

    return JsonResponse(response_data)

def testWithoutIndexLessRows(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    datum_kreiranja = request.GET.get('datum_kreiranja', '')
    
    url = f"http://localhost:8000/withoutIndexLessRows/?naziv={naziv}&cijena={cijena}&datum_kreiranja={datum_kreiranja}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena,
            'datum_kreiranja': datum_kreiranja,
        },
        'output': output,
    }
    cache_key = 'cache_key_for_GetDataWithoutIndexLessRows'
    cache.delete(cache_key)
    return JsonResponse(response_data)

def testWithIndexLessRows(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    datum_kreiranja = request.GET.get('datum_kreiranja', '')
    
    url = f"http://localhost:8000/withIndexLessRows/?naziv={naziv}&cijena={cijena}&datum_kreiranja={datum_kreiranja}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena,
            'datum_kreiranja': datum_kreiranja,
        },
        'output': output,
    }
    cache_key = 'cache_key_for_GetDataWithIndexLessRows'
    cache.delete(cache_key)
    return JsonResponse(response_data)

def testWithIndexBigCard(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    datum_kreiranja = request.GET.get('datum_kreiranja', '')
    
    url = f"http://localhost:8000/withIndexBigCard/?naziv={naziv}&cijena={cijena}&datum_kreiranja={datum_kreiranja}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena,
            'datum_kreiranja': datum_kreiranja,
        },
        'output': output,
    }
    cache_key = 'cache_key_for_GetDataWithIndexBigCard'
    cache.delete(cache_key)
    return JsonResponse(response_data)

def testWithPartIndexBigCard(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    datum_kreiranja = request.GET.get('datum_kreiranja', '')
    
    url = f"http://localhost:8000/withPartIndexBigCard/?naziv={naziv}&cijena={cijena}&datum_kreiranja={datum_kreiranja}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena,
            'datum_kreiranja': datum_kreiranja,
        },
        'output': output,
    }
    cache_key = 'cache_key_for_GetDataWithPartIndexBigCard'
    cache.delete(cache_key)
    return JsonResponse(response_data)

def testWithWrongIndexBigCard(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    
    url = f"http://localhost:8000/withWrongIndexBigCard/?naziv={naziv}&cijena={cijena}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena
        },
        'output': output,
    }
    cache_key = 'cache_key_for_GetDataWithWrongIndexBigCard'
    cache.delete(cache_key)
    return JsonResponse(response_data)

def testWithIndexDate(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    
    url = f"http://localhost:8000/withIndexDate/?naziv={naziv}&cijena={cijena}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena
        },
        'output': output,
    }
    cache_key = 'cache_key_for_GetDataWithIndexDate'
    cache.delete(cache_key)
    return JsonResponse(response_data)

def testWithIndexBigDate(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    
    url = f"http://localhost:8000/withIndexBigDate/?naziv={naziv}&cijena={cijena}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena
        },
        'output': output,
    }
    cache_key = 'cache_key_for_GetDataWithIndexBigDate'
    cache.delete(cache_key)
    return JsonResponse(response_data)

def testWithWrongIndexFull(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    datum_kreiranja = request.GET.get('datum_kreiranja', '')
    
    url = f"http://localhost:8000/withWrongIndexFull/?naziv={naziv}&cijena={cijena}&datum_kreiranja={datum_kreiranja}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena,
            'datum_kreiranja': datum_kreiranja,
        },
        'output': output,
    }
    cache_key = 'cache_key_for_GetDataWithWrongIndexFull'
    cache.delete(cache_key)
    return JsonResponse(response_data)

def testWithWrongIndexBigCardFull(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    datum_kreiranja = request.GET.get('datum_kreiranja', '')
    
    url = f"http://localhost:8000/withWrongIndexBigCardFull/?naziv={naziv}&cijena={cijena}&datum_kreiranja={datum_kreiranja}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena,
            'datum_kreiranja': datum_kreiranja,
        },
        'output': output,
    }
    cache_key = 'cache_key_for_GetDataWithWrongIndexBigCardFull'
    cache.delete(cache_key)
    return JsonResponse(response_data)