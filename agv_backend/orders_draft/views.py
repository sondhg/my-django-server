# orders_draft/views.py

from rest_framework import generics

from .models import OrderDraft
from .serializers import OrderDraftSerializer


class OrderDraftListCreate(generics.ListCreateAPIView):
    queryset = OrderDraft.objects.all().order_by('order_date', 'start_time')
    serializer_class = OrderDraftSerializer


class OrderDraftRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDraft.objects.all().order_by('order_date', 'start_time')
    serializer_class = OrderDraftSerializer
