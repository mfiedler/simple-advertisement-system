from django.db import models
from django.forms import ModelForm


class Entry(models.Model):
	description = models.TextField();
	publication_date = models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		from django.core.urlresolvers import reverse
		return reverse('entry_detail', args=[str(self.id)])
