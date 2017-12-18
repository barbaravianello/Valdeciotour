from django import forms
from django.core.mail import send_mail
from django.conf import settings 
from . import views


class ContactValdeciotour(forms.Form):
	name = forms.CharField(label = 'Nome', widget=forms.TextInput(attrs={'class':'col-xs-12 col-sm-12 col-md-12 col-lg-12', 'placeholder':'Nome', 'required':'required'}))
	email = forms.EmailField(label = 'E-mail', widget=forms.TextInput(attrs={'class':'col-xs-12 col-sm-12 col-md-12 col-lg-12', 'placeholder':'seuemail@gmail.com', 'required':'required', 'type': 'email'}) )
	message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'class':'col-xs-12 col-sm-12 col-md-12 col-lg-12', 'rows': 5, 'cols': 20 ,'placeholder':'Escreva sua mensagem', 'required':'required'}))

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