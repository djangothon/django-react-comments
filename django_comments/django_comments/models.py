from django.db import models

class Save_comments(models.Model):
	user_id = models.CharField(max_length=250)
	post_id = models.CharField(max_length=250)
	comment = models.CharField(max_length=500)
	
	def __str__(self):
		return self.title
