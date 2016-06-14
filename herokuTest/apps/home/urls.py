# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, static
from .views import Home, Contact, ContestBasis, Training, Conditions

urlpatterns = [
	url(r'^$', Home.as_view(), name='home'),
	url(r'^bases$', ContestBasis.as_view(), name='bases'),
	url(r'^contactanos/$', Contact.as_view(), name='contact'),
	url(r'^entrenamiento/$', Training.as_view(), name='training'),
	url(r'^terminosycondiciones/$', Conditions.as_view(), name='terminos'),
]
