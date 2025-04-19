# hr/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("nhap-nhan-vien/", views.nhap_nhan_vien, name="nhap_nhan_vien"),
]
