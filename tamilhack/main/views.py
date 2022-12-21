from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from difflib import SequenceMatcher

# import wikipedia
# from translate import Translator


def home(request):
    qwe = "book"
    # translator=Translator(to_lang="ta")
    # res=translator.translate(qwe,dest="ta")
    res = "testing0"
    return render(request, "home.html", {"res": res, "qwe": qwe})


'''
translator= Translator(to_lang="ta")
    
    wikipedia.set_lang("en")
    result1 = query
    result2 = wikipedia.summary(cause_query,sentences=2)
    result3 = wikipedia.summary(symp_query,sentences=2)
    result4 = wikipedia.search(rel_dis,results=5)
    translation4=[]
    translation1 = translator.translate(result1)
    translation2 = translator.translate(result2)
    translation3 = translator.translate(result3)
'''

# API


@api_view(['GET'])
def Adiseases(request):
    diseases = Disease.objects.all()
    serializer = DiseaseSerializer(diseases, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Lookseases(request, name):
    data = request.data
    adiseases = Disease.objects.all()
    #SequenceMatcher(None, a, b).ratio()
    #diseases = Disease.objects.get(name=name)
    diseases = []
    for i in adiseases:
        print("the name:", name, "compname", i.name)
        print(SequenceMatcher(None, name, i.name).ratio())
        if (SequenceMatcher(None, name, i.name).ratio() >= 0.6 or SequenceMatcher(None, name, i.tname).ratio() >= 0.55):
            diseases = Disease.objects.get(pk=i.id)
            print("disease in list", diseases)
            print("the name:", name, "compname", i.name)
    seri = DiseaseSerializer(diseases, many=False)
    return Response(seri.data)
# def Lookseases(request, name):
#     data = request.data
#     diseases = Disease.objects.get(name=name)
#     seri = DiseaseSerializer(diseases, many=False)
#     return Response(seri.data)


@api_view(['GET'])
def organView(request):
    orgs = organwise.objects.all()
    seri = OrganSerializer(orgs, many=True)
    return Response(seri.data)


@api_view(['GET'])
def newsView(request):
    new = news.objects.all()
    seri = NewsSerializer(new, many=True)
    return Response(seri.data)


@api_view(['GET'])
def desbysymp(request, symp):
    adiseases = Disease.objects.all()
    print("symp sent:", symp)
    for i in adiseases:
        flag = 0
        t0 = i.symptoms.lower()
        t1 = i.symptoms1.lower()
        t2 = i.symptoms2.lower()
        t3 = i.symptoms3.lower()
        t4 = i.symptoms4.lower()
        try:
            symp = symp.lower()
        except:
            symp = str(symp)
        print(symp, " ", t0)
        print(symp, " ", t1)
        print(symp, " ", t2)
        print(symp, " ", t3)
        print(symp, " ", t4)
        if (str(symp) in str(t0) or str(symp) == str(t0)):
            flag += 1
        if (str(symp) in str(t1) or str(symp) == str(t1)):
            flag += 1
        if (str(symp) in str(t2) or str(symp) == str(t2)):
            flag += 1
        if (str(symp) in str(t3) or str(symp) == str(t3)):
            flag += 1
        if (str(symp) in str(t4) or str(symp) == str(t4)):
            flag += 1
        if (flag < 1):
            adiseases = adiseases.exclude(pk=i.id)
        print("dtname:", i.tname)
    serializer = DiseaseSerializer(adiseases, many=True)
    return Response(serializer.data)
