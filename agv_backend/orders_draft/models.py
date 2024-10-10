from django.db import models


class OrderDraft(models.Model):
    id = models.BigAutoField(primary_key=True)
    agv_id = models.IntegerField()
    order_date = models.DateField()
    start_time = models.TimeField()  # Updated to TimeField
    start_point = models.IntegerField()
    end_point = models.IntegerField()
    load_name = models.CharField(max_length=100)
    load_amount = models.IntegerField()

    def __str__(self):
        return f"Order {self.id} for AGV {self.agv_id}"
