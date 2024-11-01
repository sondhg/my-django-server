from django.urls import path

from . import views

urlpatterns = [
    path("agvs/", views.agv_list, name="agv_list"),
    path("agvs/<int:agv_id>/", views.agv_detail, name="agv_detail"),
]