from django.db import models


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Repo(models.Model):
	repo_url = models.CharField(max_length=1000)
	#Repo.save()


	def __str__(self):
		return self.repo_url