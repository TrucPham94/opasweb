from django.contrib import admin
from .models import NganhHang, SanPham, AboutUs, ThongBao, Banner


# Register your models here.
class NganhHangAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "fullname", "status", "ngay_bat_dau")
    list_filter = ("status",)
    search_fields = ("name", "address", "fullname")
    list_editable = ("status",)


admin.site.register(NganhHang, NganhHangAdmin)


# San Pham
class SanPhamAdmin(admin.ModelAdmin):
    list_display = ("name", "nganh_hang", "status")
    # list_filter = ("nganh_hang", "status")


admin.site.register(SanPham, SanPhamAdmin)


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("title", "content")
    search_fields = ("title",)


admin.site.register(AboutUs, AboutUsAdmin)


# Thông báo
class ThongBaoAdmin(admin.ModelAdmin):
    list_display = (
        "loai_bai_viet",
        "tieu_de",
        "ngay_dang",
    )

    # search_fields = ("title",)


admin.site.register(ThongBao, ThongBaoAdmin)


# Banner
class BannerAdmin(admin.ModelAdmin):
    list_display = ("id", "status")
    list_filter = ("status",)


admin.site.register(Banner, BannerAdmin)
