from django import forms
from .models import Field, Culture, SeedProcess
from django.forms.widgets import TextInput

class SeedForm(forms.ModelForm):
    seedDate = forms.DateField(widget = forms.DateInput(attrs={'type': 'date'}), label='Дата посіву')
    harvestDate = forms.DateField(widget = forms.DateInput(attrs={'type': 'date'}), label='Очікувана дата збору')
    field = forms.ModelChoiceField(queryset= Field.objects.all(), label='Поле')
    culture = forms.ModelChoiceField(queryset= Culture.objects.all(), label='Культура')

    class Meta:
        model = SeedProcess
        fields = ['seedDate', 'harvestDate', 'field', 'culture']

class FieldForm(forms.ModelForm):
    title = forms.CharField(max_length=16, label='Назва')
    square = forms.FloatField(required=False, label='Площа')
    polygon = forms.CharField(max_length=256, label='Контур')

    class Meta:
        model = Field
        fields = ['title', 'polygon', 'square']

class CultureForm(forms.ModelForm):
    name = forms.CharField(max_length=32, label='Назва')
    class Meta:
        model = Culture
        fields = ['name', 'color']
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }
        
		