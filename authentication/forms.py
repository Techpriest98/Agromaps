from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Логін')
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Користувача з даними логіном та паролем не знайдено')
            if not user.check_password(password):
                raise forms.ValidationError('Пароль введено не коректно')
            if not user.is_active:
                raise forms.ValidationError('Акаунт з даними логіном та паролем не активовано')

            return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label='Email адреса')
	email2 = forms.EmailField(label='Підтвердіть email')
	pasword = forms.CharField(widget=forms.PasswordInput)

	class Meta:
	    model = User
	    fields = [
	        'username',
	        'email',
	        'email2',
	        'password'
	    ]
	
	def clean_email():
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError('Email адреси не співпадають')
		email_query_set = User.objects.filter(email=email)
		if email_query_set.exists():
		    raise forms.ValidationError('Користувач з такою email адресою вже існує')
		return email