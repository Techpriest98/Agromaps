from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Field, Culture, Process, SeedProcess
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import  FieldSerializer, CultureSerializer, SeedSerializer

from django.views import View
from .forms import SeedForm, FieldForm, CultureForm
from django.http import HttpResponseRedirect


@login_required
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

@login_required
def detail(request, seed_id):
    seed = get_object_or_404(SeedProcess, pk=seed_id)
    field = get_object_or_404(Field, pk=seed.field.pk)
    culture = get_object_or_404(Culture, pk=seed.culture.pk)

    context = {
        'seed' : seed,
        'field' : field,
        'culture' : culture,
    }

    return render(request, 'map/seed_detail.html', context)

@login_required
def fields(request):
  
    fields = Field.objects.all()

    context = {
        'fields' : fields
    }

    return render(request, 'map/fields.html', context)

@login_required
def cultures(request):
    cultures = Culture.objects.all()

    context = {
        'cultures' : cultures
    }

    return render(request, 'map/cultures.html', context)

class FieldsListView(generics.ListAPIView):
    """docstring for FieldsListView"""
    lookup_field = 'pk'
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = (IsAuthenticated,)
		
class CultureListView(generics.ListAPIView):
	lookup_field = 'pk'
	queryset = Culture.objects.all()
	serializer_class = CultureSerializer
	permission_classes = (IsAuthenticated,)

class SeedListView(generics.ListAPIView):
    lookup_field = 'pk'
    queryset = SeedProcess.objects.all()
    serializer_class = SeedSerializer
    permission_classes = (IsAuthenticated,)

class SeedView(View):
    decorators = [login_required]
    
    @method_decorator(decorators)
    def get(self, request, id=None, seed_id=None):  
        if id != None or seed_id != None:
            seed = get_object_or_404(SeedProcess, pk=seed_id)
            seed_form = SeedForm(instance=seed)
            template = 'seed_edit.html'
        else:
            seed_form = SeedForm(instance=SeedProcess())
            template = 'seed_new.html'
        context = {'seed_form': seed_form}
        return render(request, template, context)

    @method_decorator(decorators)
    def post(self, request, id=None, seed_id=None):
        context = {}
        method = self.request.POST.get('_method', '').lower()
        print(method)
        if id != None or seed_id != None:
            if method == 'put':
                return self.put(request, id, seed_id)
            elif method == 'delete':
                return self.delete(request, id)
        seed_form = SeedForm(request.POST, instance=SeedProcess())
        if seed_form.is_valid():
            new_seed = seed_form.save(commit=False)
            new_seed.save()
            return HttpResponseRedirect('/map/')
        context = {'seed_form' : seed_form}
        return render(request, 'seed_new.html', context)

    @method_decorator(decorators)
    def put(self, request, id=None, seed_id= None):
        context = {}
        print('put field')
        seed = get_object_or_404(SeedProcess, pk=seed_id)
        seed_form = SeedForm(request.POST, instance=seed)
        if seed_form.is_valid():
            new_seed = seed_form.save(commit=False)
            new_seed.save()
            return HttpResponseRedirect('/map/')
        context = {'seed_form' : seed_form}
        return render(request, 'seed_edit.html', context) 

    # def delete(self, request, id=None):
    #     post = get_object_or_404(Post, pk=id)
    #     post_form = DeletePostForm(request.POST, instance=post)
    #     if post_form.is_valid():
    #         post.delete()
    #         return HttpResponseRedirect('/news/')
    #     return render(request, 'post_delete.html', {})

class FieldView(View):
    decorators = [login_required]
    
    @method_decorator(decorators)
    def get(self, request, id=None, field_id=None):  
        if id != None or field_id != None:
            field = get_object_or_404(Field, pk=field_id)
            field_form = FieldForm(instance=field)
            template = 'field_edit.html'
        else:
            field_form = FieldForm(instance=Field())
            template = 'field_new.html'
        context = {'field_form': field_form}
        return render(request, template, context)

    @method_decorator(decorators)
    def post(self, request, id=None):
        context = {}
        method = self.request.POST.get('_method', '').lower()
        print(method)
        if id != None:
            if method == 'put':
                return self.put(request, id)
            elif method == 'delete':
                return self.delete(request, id)
        field_form = FieldForm(request.POST, instance=Field())
        if field_form.is_valid():
            new_field = field_form.save(commit=False)
            new_field.save()
            return HttpResponseRedirect('/map/fields/')
        context = {'field_form' : field_form}
        return render(request, 'field_new.html', context)

    @method_decorator(decorators)
    def put(self, request, id=None):
        context = {}
        print('put field')
        seed = get_object_or_404(Seed, pk=id)
        seed_form = SeedForm(request.POST, instance=seed)
        if seed_form.is_valid():
            new_seed = post_form.save(commit=False)
            new_seed.save()
            return HttpResponseRedirect('/map/')
        context = {'seed_form' : seed_form}
        return render(request, 'seed_edit.html', context)	

class CultureView(View):
    decorators = [login_required]
    
    @method_decorator(decorators)
    def get(self, request, id=None, culture_id=None):  
        if id != None or culture_id != None:
            culture = get_object_or_404(Culture, pk=culture_id)
            culture_form = CultureForm(instance=culture)
            template = 'culture_edit.html'
        else:
            culture_form = CultureForm(instance=Culture())
            template = 'culture_new.html'
        context = {'culture_form': culture_form}
        return render(request, template, context)

    @method_decorator(decorators)
    def post(self, request, id=None, culture_id=None):
        context = {}
        method = self.request.POST.get('_method', '').lower()
        if id != None or culture_id != None:
            print(method)
            if method == 'put':
                return self.put(request, culture_id)
            elif method == 'delete':
                return self.delete(request, id)
        culture_form = CultureForm(request.POST, instance=Culture())
        if culture_form.is_valid():
            new_culture = culture_form.save(commit=False)
            new_culture.save()
            return HttpResponseRedirect('/map/cultures/')
        context = {'culture_form' : culture_form}
        return render(request, 'culture_new.html', context)

    @method_decorator(decorators)
    def put(self, request, id=None):
        context = {}
        culture = get_object_or_404(Culture, pk=id)
        culture_form = CultureForm(request.POST, instance=culture)
        if culture_form.is_valid():
            new_culture = culture_form.save(commit=False)
            new_culture.save()
            return HttpResponseRedirect('/map/cultures/')
        context = {'culture_form' : culture_form}
        return render(request, 'culture_edit.html', context)   