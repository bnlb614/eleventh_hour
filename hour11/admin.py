from django.contrib import admin
from hour11.models import User11Hour

# class User11HourAdmin(admin.ModelAdmin):
# 	fieldsets = [
# 		("User name", {'fields': ['username']}),
# 		('Date Information', {'fields':['signup_date']}),
# 		("sex", {'fields':['sex']})
# 	]
# 	list_display = ('username','signup_date','sex')

# 	search_fields = ['username']

admin.site.register(User11Hour)