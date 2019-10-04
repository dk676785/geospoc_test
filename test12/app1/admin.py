from django.contrib import admin
from app1.models import UserProfile

class UserAdmin(admin.ModelAdmin):
	list_display = ['user','name','cover_letter','attachment']


admin.site.register(UserProfile,UserAdmin)
