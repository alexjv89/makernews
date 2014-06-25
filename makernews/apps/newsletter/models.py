from django.db import models

# Create your models here.
class Newsletter(models.Model):
	number = models.IntegerField()
	released_date = models.DateField('released date')
	added_time = models.DateTimeField('added time')
	link=models.URLField(max_length=1000)
	is_enabled = models.BooleanField(default = True)
	score = models.IntegerField(default = 0)
	
	class Meta:
		app_label = 'newsletter'
	def __unicode__(self):
		return str(self.number)