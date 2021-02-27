from django.db import models

class ConferenceType(models.Model):
	conference_type = models.CharField(max_length=200)

	def __str__(self):
		return self.conference_type

	class Meta:
		ordering = ['conference_type']

# Create your models here.
class Conference(models.Model):
	name = models.CharField(max_length=200)
	start = models.DateField()
	end = models.DateField()
	conference_type = models.ForeignKey(ConferenceType, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']

class Pillar(models.Model):
	name = models.CharField(max_length=200)
	conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']

class Session(models.Model):
	name = models.TextField()
	conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
	pillar = models.ForeignKey(Pillar, on_delete=models.SET_NULL, blank=True, null=True)
	summary = models.TextField()
	number = models.IntegerField()

	def __str__(self):
		return "{}: {}".format(self.number, self.name)

	class Meta:
		ordering = ['number']

class Company(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']

class Speaker(models.Model):
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	details = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']

class Speech(models.Model):
	session = models.ForeignKey(Session, on_delete=models.CASCADE)
	speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)

	class Meta:
		ordering = ['speaker']


class KeyTakeaway(models.Model):
	session = models.ForeignKey(Session, on_delete=models.CASCADE)
	takeaway = models.TextField()

class Quote(models.Model):
	session = models.ForeignKey(Session, on_delete=models.CASCADE)
	speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
	quote = models.TextField() 
