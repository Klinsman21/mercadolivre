from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from django.db import models

class Produto(models.Model):
	name = models.CharField(max_length=255, blank=False, verbose_name='nome')
	keyword = models.CharField(max_length=255, blank=False, verbose_name='palavra chave')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	startPrice = models.PositiveIntegerField(validators=[MinValueValidator(0)], verbose_name='lançe inicial', default=0)
	ultimoLance = models.PositiveIntegerField(validators=[MinValueValidator(0)], verbose_name='lançe final', default=0)
	Prazo = models.DateField(blank=False,verbose_name='prazo')
	vendido = models.BooleanField(default=False, verbose_name='vendido')
	compradoPor = models.CharField(max_length=255, blank=False, verbose_name='nomeComprador')
	state = models.BooleanField(default=True, verbose_name='ativo')
	image = models.ImageField(blank=True)

	def __str__(self):
		return 'produto'

	class Meta:
		verbose_name = 'produto'
		verbose_name_plural = 'produtos'

class Lance(models.Model):
	produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	lance = models.PositiveIntegerField(validators=[MinValueValidator(0)], verbose_name='lançe', default=0)
	bought = models.BooleanField(default=False, verbose_name='comprado')

	def __str__(self):
		return 'Lançes'

	class Meta:
		verbose_name = 'lançe'
		verbose_name_plural = 'lançes'


