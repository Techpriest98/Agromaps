from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Field, Culture, Process

def index(request):

    fields = Field.objects.all()
    
    
    context = {
        'title' : 'All fields',
        'fields' : fields
    }
    
    return render(request, 'map/index.html', context)

def detail(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    culture = get_object_or_404(Culture, pk=field.cultureID_id)
    process = get_object_or_404(Process, pk=field.process_id)
    
    context = {
        'field' : field,
        'culture' : culture,
        'process' : process
    }
    
    return render(request, 'map/field_detail.html', context)
