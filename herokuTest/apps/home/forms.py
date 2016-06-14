# -*- coding: utf-8 -*-
from django import forms


class ContactForm(forms.Form):
	messages = {
		'required': "Este campo es requerido"
	}

	name    = forms.CharField( error_messages={'required': messages['required']} )
	email   = forms.EmailField( error_messages={'required': messages['required']} )
	message = forms.CharField( error_messages={'required': messages['required']} )


