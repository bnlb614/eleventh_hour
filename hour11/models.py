from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class User11Hour(models.Model):
	user = models.OneToOneField(User)

	sex = models.CharField(max_length = 200, blank=True) #blank = True allows for this field to be left blank
	pub_date = models.DateTimeField('date created')
	#I'll deal with pictures later.
	# picture = models.ImageField(upload_to = 'profile_images',blank=True)

	def __unicode__(self):
		return self.user.username