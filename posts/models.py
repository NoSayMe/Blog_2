from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=2000)
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
    votes_total = models.IntegerField(default=1)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
