from django import forms
from . import models
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class ProductForm(forms.ModelForm):

	#finalDate = DateField(widget=AdminDateWidget)
	class Meta:
		model = models.Produto
		fields = ('name', 'keyword', 'image', 'startPrice', 'Prazo',)