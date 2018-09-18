from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect
import random
from datetime import date
from django.urls import reverse_lazy

from . import models, forms

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class CreateProduct(generic.CreateView):
	form_class = forms.ProductForm
	success_url = reverse_lazy('home')
	template_name = 'produto.html'
	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = models.User.objects.get(id=self.request.user.pk)
		obj.save()
		return super(CreateProduct, self).form_valid(form)

class Search(generic.ListView):
	model = models.Produto
	template_name = 'home.html'
	def get_queryset(self):
		if(len(models.Produto.objects.filter(keyword=self.request.GET['q']))):
			return models.Produto.objects.filter(keyword=self.request.GET['q'])
		else:
			lista = [False]
			return lista

class Throw(generic.ListView):
	model = models.Produto
	template_name = 'home.html'
	def get(self, request):
		print(self.request.GET['lance'])
		print(self.request.GET['id'])
		if(models.Lance.objects.filter(user=models.User.objects.get(id=self.request.user.pk), produto=models.Produto.objects.get(id=self.request.GET['id']))):
			models.Lance.objects.filter(produto=models.Produto.objects.get(id=self.request.GET['id'])).update(lance=self.request.GET['lance'])
			models.Produto.objects.filter(id=self.request.GET['id']).update(ultimoLance=self.request.GET['lance'])
		else:
			lance = models.Lance.objects.create(produto=models.Produto.objects.get(id=self.request.GET['id']), user=models.User.objects.get(id=self.request.user.pk), lance=int(self.request.GET['lance']))
			lance.save()
			models.Produto.objects.filter(id=self.request.GET['id']).update(ultimoLance=self.request.GET['lance'])
		return HttpResponseRedirect('/')


class Home(generic.ListView):
	model = models.Produto
	template_name = 'home.html'
	def get_queryset(self):
		dateAtual = date.today()
		for x in models.Produto.objects.all():
			if(x.state == True):
				if(x.Prazo < dateAtual):
					obj = models.Produto.objects.get(id=x.id)
					models.Produto.objects.filter(id=x.id).update(state=False, vendido=True)
					values = models.Produto.objects.get(id=x.id).ultimoLance
					models.Lance.objects.filter(produto=obj, lance=values).update(bought=True)

		return models.Produto.objects.all()

class MeusLances(generic.ListView):
	model = models.Lance
	template_name = 'lances.html'
	def get_queryset(self):
		if(len(self.request.GET) > 0):
			print(self.request.GET['id'])
			models.Lance.objects.filter(id=self.request.GET['id']).delete()
		return models.Lance.objects.filter(user=models.User.objects.get(id=self.request.user.pk))


class MyProduct(generic.ListView):
	model = models.Produto
	template_name = 'myproduct.html'
	def get_queryset(self):
		if(len(self.request.GET) > 0):
			models.Produto.objects.filter(id = self.request.GET['id']).delete()

		return models.Produto.objects.filter(user=models.User.objects.get(id=self.request.user.pk))

class ProductUp(UpdateView):

    model = models.Produto
    template_name = 'produto.html'
    success_url = reverse_lazy('leilao:my')
    form_class = forms.ProductForm