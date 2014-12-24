from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInlineStacked(admin.StackedInline):
	#stacks 'extra' number of choices in each question
	model = Choice
	extra = 3

class ChoiceInlineTabular(admin.TabularInline):
	#makes a little table of 'extra' number of choices in each question
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
			(None, 				{'fields': ['question_text']}),
			('Date Information', {'fields':['pub_date']})
	]
	# inlines = [ChoiceInlineStacked]
	inlines = [ChoiceInlineTabular]
	#below tuple makes it so we display question text and publication data in two columns on main admin page.
	list_display = ('question_text','pub_date')
	#below make a search box. Magic
	search_fiels = ['question_text']



admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
# Register your models here.
