from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	#return HttpResponse('<h1>Hello, World!</h1>')
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
		'my_text': 'this is about us <3',
		'my_number': 123,
		'this_is_true': True,
		'my_list':[1,123,12345,1234567]
	}
	return render(request, "about.html", my_context)
