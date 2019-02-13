from django.db import models

# Create your models here.
class List(models.Model):
	item=models.TextField(max_length=120)
	completed=models.BooleanField(default=False)

	def __str__(self):
		return self.item+' | '+str(self.completed) 