# orders_draft/models.py

from django.db import models


class OrderDraft(models.Model):
    agv_id = models.IntegerField()
    order_date = models.CharField(max_length=10)
    start_time = models.CharField(max_length=8)
    start_point = models.CharField(max_length=2)
    end_point = models.CharField(max_length=2)
    load_name = models.CharField(max_length=100)
    load_amount = models.IntegerField()

    def __str__(self):
        return f"Order {self.id} for AGV {self.agv_id}"
