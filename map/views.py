from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Field, Culture, Process, SeedProcess
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import  FieldSerializer, CultureSerializer, SeedSerializer

def index(request):

    seeds = SeedProcess.objects.all()
    fields = []
    for seed in seeds:
    	fields.append(Field.objects.get(pk=seed.field.pk))
    	
    context = {
    	'seeds' : seeds,
        'fields' : fields
    }
    
    return render(request, 'map/index.html', context)

def detail(request, seed_id):
    seed = get_object_or_404(SeedProcess, pk=seed_id)
    field = get_object_or_404(Field, pk=seed.field.pk)
    culture = get_object_or_404(Culture, pk=field.cultureID_id)
    process = get_object_or_404(Process, pk=field.process_id)

    context = {
        'fields' : field,
        'cultures' : culture,
        'processes' : process
    }

    return render(request, 'map/field_detail.html', context)


class FieldsListView(generics.ListAPIView):
    """docstring for FieldsListView"""
    lookup_field = 'pk'

    def getActiveFields():
        seeds = SeedProcess.objects.all()
        fields = []
        for seed in seeds:
            fields.append(Field.objects.get(pk=seed.field.pk))
        return fields

    queryset = getActiveFields()
    serializer_class = FieldSerializer
    permission_classes = (IsAdminUser,)
		

class  CultureListView(generics.ListAPIView):
	lookup_field = 'pk'
	queryset = Culture.objects.all()
	serializer_class = CultureSerializer
	permission_classes = (IsAdminUser,)

class SeedListView(generics.ListAPIView):
    lookup_field = 'pk'
    queryset = SeedProcess.objects.all()
    serializer_class = SeedSerializer
    permission_classes = (IsAdminUser,)		