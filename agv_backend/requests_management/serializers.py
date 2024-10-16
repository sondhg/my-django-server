from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateField(
        format="%m/%d/%Y", input_formats=["%m/%d/%Y"]  # Capital "Y" means 4-digit year
    )
    start_time = serializers.TimeField(
        format="%H:%M:%S", input_formats=["%H:%M:%S"]
    )  # Ensure correct format

    class Meta:
        model = Order
        fields = "__all__"
