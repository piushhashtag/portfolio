from django.db import models

# Create your models here.
class File(models.Model):
	file = models.FileField(null=True, blank=True)

	def __str__(self):
		return str(self.file)


class Contact(models.Model):
	name=models.CharField(max_length=200)
	email=models.EmailField()
	message=models.TextField()

	def __str__(self):
		return str(self.name)