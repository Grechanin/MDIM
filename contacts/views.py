from django.shortcuts import render, get_object_or_404
from .models import Contacts

def contacts(request):
	contacts = Contacts.objects.filter(is_active=True)[0]

	
	context = {
			'contacts': contacts,
		}

	return render(request, 'contacts/contacts.html', context)