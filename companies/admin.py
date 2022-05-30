from django.contrib import admin

# Register your models here.
from companies.models import Companies, TagLang

admin.site.register([Companies, TagLang])
