from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Package(models.Model):
	title = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')
	description = RichTextField('Descrição')
	price = models.DecimalField('Preço', max_digits=7, decimal_places=2)
	travel_date = models.DateField('Data da Partida', null=True, blank=True)
	arrival_date = models.DateField('Data da Chegada', null=True, blank=True)
    
	ida = 'ida'
	idavolta = 'idavolta'

	TRAVEL_CHOICES = (
		(ida, "Viagem apenas de ida"),
		(idavolta, "Viagem de ida e volta"),
	)

	travel_type = models.CharField('Tipo da Viagem', max_length=50, choices = TRAVEL_CHOICES, default=ida)
	image = models.ImageField(upload_to='package/images', verbose_name='Foto', default='media/images/1.jpg')
	created_at = models.DateTimeField('Criado em', auto_now_add = True)
	updated_at = models.DateTimeField('Atualizado em', auto_now = True)
	prepopulated_fields = {'slug': ['title']}

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Pacote'
		verbose_name_plural = 'Pacotes'
		ordering = ['title']

class Gallery(models.Model):
	title = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')
	description = RichTextField('Descrição')
	travel_date = models.DateField('Data da Partida', null=True, blank=True)
	arrival_date = models.DateField('Data da Chegada', null=True, blank=True)
	image = models.ImageField(upload_to='package/images', verbose_name='Foto', default='media/images/1.jpg')
	created_at = models.DateTimeField('Criado em', auto_now_add = True)
	updated_at = models.DateTimeField('Atualizado em', auto_now = True)
	prepopulated_fields = {'slug': ['title']}

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Galeria'
		verbose_name_plural = 'Galerias'
		ordering = ['title']