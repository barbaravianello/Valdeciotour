from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Package(models.Model):
	title = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')
	description = RichTextField('Descrição')
	price = models.DecimalField('Preço', max_digits=7, decimal_places=2)
	travel_date = models.DateField('Data da Viagem', null=True, blank=True)
	image = models.ImageField(upload_to='package/images', verbose_name="Foto", null=True, blank=True)
	created_at = models.DateTimeField('Criado em', auto_now_add = True)
	updated_at = models.DateTimeField('Atualizado em', auto_now = True)
	prepopulated_fields = {'slug': ['title']}

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Pacote'
		verbose_name_plural = 'Pacotes'
		ordering = ['title']