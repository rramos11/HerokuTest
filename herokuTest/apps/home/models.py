from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings


class Image(models.Model):
	file = models.ImageField(upload_to=settings.MEDIA_ROOT, null=True);

	def __unicode__(self):
		return self.file.name


class SliderItem(models.Model):
	title = models.TextField(null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	image = models.ForeignKey(Image, default=None)
	creation_date = models.DateTimeField(editable=False, default=timezone.now)

	def __unicode__(self):
		if not self.title:
			return self.image
		return self.title

	def save(self, *args, **kwargs):
		return super(SliderItem, self).save(*args, **kwargs)


class SliderItemLink(models.Model):
	title = models.TextField(null=True, blank=True)
	url = models.URLField(null=True, blank=True)
	sliderItem = models.ForeignKey(SliderItem, default=None)

	def __unicode__(self):
		return self.title
