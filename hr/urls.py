# hr/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("nhap-nhan-vien/", views.nhap_nhan_vien, name="nhap_nhan_vien"),
    path("danh_sach_nhan_vien/", views.danh_sach_nhan_vien, name="danh_sach_nhan_vien"),
    path("tai-danh-sach/", views.export_nhan_vien_excel, name="tai_danh_sach"),
    path("danh-sach/<int:pk>/", views.profile_nhan_vien, name="chi_tiet_nhan_vien"),
    path("bao-cao/", views.bao_cao_nhan_su, name="bao_cao_nhan_su"),
]
