from django.shortcuts import render
from home.models import Package, Gallery
from .forms import ContactValdeciotour, LeadForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect

from social_django.models import UserSocialAuth


def index(request): 

	packages = Package.objects.all()
	gallery = Gallery.objects.all()
	
	context = {
		'packages': packages,
        'gallery': gallery,
	}
	
	if request.method == 'POST':
		form = ContactValdeciotour(request.POST or None)
		subform = LeadForm(request.POST or None)
		if form.is_valid():
			context['is_valid'] = True
			form.send_mail()
			form = ContactValdeciotour()
		if subform.is_valid():
			context['is_valid'] = True
			subform.save_contact()
			subform = LeadForm()
	else:
		form = ContactValdeciotour()
		subform = LeadForm()
	context['form'] = form
	context['subform'] = subform
	
	return render(request, "home/index.html", context)


@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'core/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'core/password.html', {'form': form})
