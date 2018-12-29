from django import forms
from .models import Post, Corp, Preview

class CorpForm(forms.ModelForm):
    name = forms.CharField(max_length=64, label="Назва підприємства")
    email = forms.EmailField(max_length=32, label= "Контактна пошта")
    phone = forms.CharField(max_length=12, label="Контактний телефон")
	
    class Meta:
        model = Corp
        fields = ['name', 'email', 'phone']

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label="Заголовок")
    datetime = forms.DateTimeField(label='Час публікації')
    content = forms.CharField(widget=forms.Textarea, max_length=10000, label='Зміст публікації')
    preview = forms.ModelChoiceField(queryset=Preview.objects.all(), label='Зображення')
	
    class Meta:
        model = Post
        fields = ['title', 'datetime', 'content', 'preview']

class DeletePostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = []
			
		


			

