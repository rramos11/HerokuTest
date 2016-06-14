from django.shortcuts import render
from django.views.generic import View
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.shortcuts import redirect

from .forms import ContactForm
from .models import SliderItem, SliderItemLink, Image


# Create your views here.
class Home(View):
	def get(self, request):
		slider_items = SliderItem.objects.all()
		for item in slider_items:
			item.links = SliderItemLink.objects.filter(sliderItem__id=item.id).order_by('-title')
			img = Image.objects.filter(id=item.image_id)
			item.background_image = str.split(str(img[0].file.name), "/")[-1] if img else 'noImage.jpg'

		return render(request, "home.index.html", {'slider_items': slider_items})


class ContestBasis(View):
	def get(self, request):
		return render(request, "bases.html", {})


class Contact(View):
	def get(self, request):
		return render(request, "contact.us.html", {})

	def post(self, request):
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']
			subject = "Formulario de contacto (" + name + ") - Intellisys Challenge"
			context = {
				'name': name,
				'email': email,
				'message': message
			}

			message = get_template('contact.email.html').render(context=context)
			recipient_list = ['challenge@intellisys.com.do']
			msg = EmailMessage(subject, message, to=recipient_list)
			msg.content_subtype = 'html'
			msg.send()
			return redirect("/")
		return render(request, "contact.us.html", {'form': form})


class Training(View):
	def get(self, request):
		return render(request, "training.html", {})


class Conditions(View):
	def get(self, request):
		return render(request, 'terms_and_conditions.html')
