from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about-us/", views.about_us_view, name="about_us"),
    path("group/", views.group, name="group"),
    path("apply/", views.apply, name="apply"),
    path("notifications/", views.notifications, name="thong-bao"),
    path("thong-bao/<int:pk>/", views.thong_bao_chi_tiet, name="thong_bao_chi_tiet"),
    path("apply/", views.apply, name="tuyen-dung"),
    path(
        "tuyen-dung/<int:pk>/",
        views.tin_tuyen_dung_chi_tiet,
        name="tuyen_dung_chi_tiet",
    ),
]
