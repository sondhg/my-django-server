from rest_framework import serializers

from .models import OrderDraft


class OrderDraftSerializer(serializers.ModelSerializer):
    order_date = serializers.DateField(
        format="%m/%d/%Y", input_formats=["%m/%d/%Y", "%m/%d/%y"]
    )
    start_time = serializers.TimeField(
        format="%H:%M:%S", input_formats=["%H:%M:%S"]
    )  # Ensure correct format

    class Meta:
        model = OrderDraft
        fields = "__all__"
