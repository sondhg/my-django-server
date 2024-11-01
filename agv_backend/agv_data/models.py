from django.db import models

class AGVData(models.Model):
    agv_id = models.IntegerField(primary_key=True)
    max_battery = models.IntegerField()
    max_speed = models.FloatField()
    max_load = models.IntegerField()
    guidance_type = models.CharField(max_length=100)
    is_connected = models.BooleanField(default=False)
    is_busy = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"AGV {self.agv_id} - {self.guidance_type}"