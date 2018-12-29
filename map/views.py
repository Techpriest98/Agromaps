# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required

# from .models import Field, Culture, Process, SeedProcess
# from rest_framework import generics
# from rest_framework.permissions import IsAdminUser, IsAuthenticated
# from .serializers import  FieldSerializer, CultureSerializer, SeedSerializer


# @login_required
# def index(request):

#     seeds = SeedProcess.objects.all()
#     fields = []
#     for seed in seeds:
#     	fields.append(Field.objects.get(pk=seed.field.pk))
    	
#     context = {
#     	'seeds' : seeds,
#         'fields' : fields
#     }
    
#     return render(request, 'map/index.html', context)

# def detail(request, seed_id):
#     seed = get_object_or_404(SeedProcess, pk=seed_id)
#     field = get_object_or_404(Field, pk=seed.field.pk)
#     culture = get_object_or_404(Culture, pk=field.cultureID_id)
#     process = get_object_or_404(Process, pk=field.process_id)

#     context = {
#         'fields' : field,
#         'cultures' : culture,
#         'processes' : process
#     }

#     return render(request, 'map/field_detail.html', context)


# class FieldsListView(generics.ListAPIView):
#     """docstring for FieldsListView"""
#     lookup_field = 'pk'


#     def getActiveFields():
#         seeds = SeedProcess.objects.all()
#         fields = []
#         for seed in seeds:
#             fields.append(Field.objects.get(pk=seed.field.pk))
#         return fields

#     queryset = getActiveFields()
#     #queryset = Field.objects.all()
#     serializer_class = FieldSerializer
#     permission_classes = (IsAuthenticated,)
		

# class  CultureListView(generics.ListAPIView):
# 	lookup_field = 'pk'
# 	queryset = Culture.objects.all()
# 	serializer_class = CultureSerializer
# 	permission_classes = (IsAuthenticated,)

# class SeedListView(generics.ListAPIView):
#     lookup_field = 'pk'
#     queryset = SeedProcess.objects.all()
#     serializer_class = SeedSerializer
#     permission_classes = (IsAuthenticated,)		