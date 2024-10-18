from django.urls import path

from . import views

urlpatterns = [
    path("orders/", views.order_list, name="order_list"),
    path("orders/<int:id>/", views.order_detail, name="order_detail"),
]
