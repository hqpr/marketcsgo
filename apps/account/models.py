import datetime
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(default='')
    api_key = models.CharField(max_length=255)
    steam_username = models.CharField(max_length=255)
    abs_min_price = models.PositiveIntegerField()
    max_price = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.user_id or not self.created:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" % self.user
