from django.contrib import admin
from django.forms.models import BaseInlineFormSet, ModelForm

# Register your models here.
from .models import ConferenceType, Conference, Pillar, Session, Speaker, Company, KeyTakeaway, Quote, Speech

class PillarInline(admin.TabularInline):
	model = Pillar
	fields = ('name',)
	extra = 2

class SessionInline(admin.TabularInline):
	model = Session
	fields = ('name','pillar','summary')
	extra = 2

class SpeakerInline(admin.TabularInline):
	model = Speaker
	fields = ('name','title')
	extra = 2

class KeyTakeawayInline(admin.TabularInline):
	model = KeyTakeaway
	fields = ('takeaway',)
	extra = 5

class QuoteInline(admin.TabularInline):
	model = Quote
	fields = ('quote','speaker')
	extra = 3

class SpeechInline(admin.TabularInline):
	model = Speech
	fields = ('speaker',)
	extra = 6

class ConferenceAdmin(admin.ModelAdmin):
	fieldsets = [
	('About', {'fields' : ['name', 'start', 'end','conference_type']}),
	]
	inlines = [PillarInline,SessionInline]

class SpeakerAdmin(admin.ModelAdmin):
	fields = ['name','company','title']

class CompanyAdmin(admin.ModelAdmin):
	fields = ['name']
	inlines = [SpeakerInline]

class SessionAdmin(admin.ModelAdmin):
	fields = ['name','number','conference','pillar','summary']
	inlines = [SpeechInline, KeyTakeawayInline, QuoteInline]

admin.site.register(ConferenceType)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Session, SessionAdmin)
