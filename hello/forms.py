from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import Profile

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required.')
	repository = forms.CharField(max_length=300, help_text='Required. Enter Github Repository URL.')
	dag_directory_name = forms.CharField(max_length=50, help_text='Required. Enter Dag Directory Name.')

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'repository',
			'dag_directory_name',
			'password1',
			'password2'
		)



# class EditProfileForm(UserChangeForm):

# 	class Meta:
# 		model = User
# 		fields = (
# 			'first_name',
# 			'last_name',
# 		)
# 		exclude = ('password')
