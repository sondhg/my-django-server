from django.db import models


class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    order_date = models.DateField()
    start_time = models.TimeField()
    start_point = models.IntegerField()
    end_point = models.IntegerField()
    load_name = models.CharField(max_length=100)
    load_amount = models.IntegerField(default=0)
    load_weight = models.IntegerField(default=0)

    def __str__(self):
        return f"Order {self.order_id} has been created"
