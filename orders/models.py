from django.db import models
from django.contrib.sessions.models import Session
from doors.models import Door, Color


class Order(models.Model):
    session = models.ForeignKey(Session)


class Item(models.Model):
    door = models.ForeignKey(Door, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    order = models.ForeignKey(Order)

    class Meta:
        unique_together = ('door', 'color', 'order')
