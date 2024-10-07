# orders_draft/views.py

from rest_framework import generics

from .models import OrderDraft
from .serializers import OrderDraftSerializer


class OrderDraftListCreate(generics.ListCreateAPIView):
    queryset = OrderDraft.objects.all()
    serializer_class = OrderDraftSerializer


class OrderDraftRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDraft.objects.all()
    serializer_class = OrderDraftSerializer
