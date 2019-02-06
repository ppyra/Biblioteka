from django.db import models
from django.contrib.auth.models import User
from shelf.models import BookItem
from datetime import datetime

from django.utils.timezone import now
# Create your models here.

class Rental(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE)
    what = models.ForeignKey(BookItem, on_delete=models.CASCADE)
    when = models.DateTimeField(default=now) # auto_now_add=True zapisuje date podczas zapisu do bazy
                                #auto_new aktualizuje za każdym razem to pole
    returned = models.DateTimeField(null=True, blank=True) #pozwalamy na puste pole w baze i dla frontend

    def __str__(self):
        return "{who} wyporzyczył {what} dnia {when}".format(who=self.who, what = self.what, when = self.when)
