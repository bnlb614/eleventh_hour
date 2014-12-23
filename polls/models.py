from django.db import models

#Each question has multiple choices

class Question(models.Model):

	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice_text

# Create your models here.
