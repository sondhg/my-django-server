# orders_draft/urls.py

from django.urls import path

from .views import OrderDraftListCreate, OrderDraftRetrieveUpdateDestroy

urlpatterns = [
    path("<int:pk>", OrderDraftRetrieveUpdateDestroy.as_view()),
    path(
        "<int:pk>/", OrderDraftRetrieveUpdateDestroy.as_view()
    ),  # Handle trailing slash
    path("", OrderDraftListCreate.as_view()),
    path("/", OrderDraftListCreate.as_view()),  # Handle trailing slash
]
