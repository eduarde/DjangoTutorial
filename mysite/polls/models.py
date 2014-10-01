from django.db import models

import datetime
from django.utils import timezone


# Create your models here.




class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

# The code is straightforward. Each model is represented by a class
# that subclasses django.db.models.Model. Each model has a number of
# class variables, each of which represents a database field in the model.


# Some Field classes have required arguments. CharField, for example, requires
# that you give it a max_length. That’s used not only in the database schema,
# but in validation, as we’ll soon see.

# A Field can also have various optional arguments; in this case, we’ve set the
# default value of votes to 0.

# Finally, note a relationship is defined, using ForeignKey. That tells Django each
# Choice is related to a single Poll. Django supports all the common database relationships:
#  many-to-ones, many-to-manys and one-to-ones.


