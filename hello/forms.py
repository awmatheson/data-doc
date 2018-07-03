from django import forms
from . import models

from .models import Repo

class RepoForm(forms.ModelForm):
	
	class Meta:
		model = models.Repo
		fields = ['repo_url']

