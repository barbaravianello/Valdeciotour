from django import forms
from django.core.mail import send_mail
from django.conf import settings 
from . import views
from .models import Email, Package, Gallery


class ContactValdeciotour(forms.Form):
	name = forms.CharField(label = 'Nome', widget=forms.TextInput(attrs={'class':'form-group form-control', 'placeholder':'Nome', 'required':'required'}))
	email = forms.EmailField(label = 'E-mail', widget=forms.TextInput(attrs={'class':'form-group form-control', 'placeholder':'E-mail', 'required':'required', 'type': 'email'}) )
	message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'class':'col-md-12 form-group form-control', 'rows': 7, 'cols': 30 ,'placeholder':'Mensagem', 'required':'required'}))

	def send_mail(self):

		message = '--------------------------------------------------------------------------------\n'
		message += ' Novo email de contato no site Valdécio Tour \n'
		message += '--------------------------------------------------------------------------------\n'
		message += 'NOME: %(name)s \n'
		message += 'E-MAIL: %(email)s \n'
		message += 'MENSAGEM: %(message)s \n'

		context = {
			'name': self.cleaned_data['name'],
			'email': self.cleaned_data['email'],
			'message': self.cleaned_data['message'],
		}
		
		message = message % context
		
		send_mail('Contato do site Valdécio Tour', message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])


# Cria o formulario para recolher o e-mail do usuario
class LeadForm(forms.Form):

	def __init__(self, *args, **kwargs):
		super(LeadForm, self).__init__(*args, **kwargs)
		self.fields['lead_place'].choices = [('', '----------')] + [(item.id, item.title) for item in Package.objects.all()]


	lead_place = forms.ChoiceField(widget=forms.Select(choices=(), attrs={'style':'color: #6c7279; border-radius: 20px; padding-left: 5px; padding-right: 5px; width: 53%; margin-bottom: 10px;margin-top: 10px'}))
	lead_name = forms.CharField(label = "Nome", max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome'}))
	lead_email = forms.EmailField(label = "E-mail", widget=forms.TextInput(attrs={'placeholder': 'Nos informe um e-mail para contato'}))
	lead_email.clean('email@example.com')

	def save_contact(self):
		email = Email(nome=self.cleaned_data['lead_name'], email=self.cleaned_data['lead_email'], local=self.cleaned_data['lead_place'])
		email.save()
		# Envio de mensagem de boas vindas
		destino = Package.objects.get(id=email.local)
		message = "Olá, %s!\nObrigado por solicitar a reserva para %s. Em breve entraremos em contato novamente.\n\nFavor não responder este email." %(email.nome, str(destino))

		send_mail('Confirmação de envio - Valdecio Tour', message,
			settings.DEFAULT_FROM_EMAIL, [email.email])
		
		message2 = "Olá!\n Novo lead %s, solicitou reserva para %s. E-mail para contato: %s." %(email.nome, str(destino), email.email)
		
		send_mail('Reserva do site Valdécio Tour', message2, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])

	def __str__(self):
		return self.lead_name