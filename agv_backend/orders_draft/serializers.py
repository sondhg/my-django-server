# orders_draft/serializers.py

from rest_framework import serializers

from .models import OrderDraft


class OrderDraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDraft
        fields = "__all__"
