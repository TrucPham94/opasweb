from django.contrib import admin
from .models import NhanVien
from django.utils.formats import date_format


class NhanVienAdmin(admin.ModelAdmin):
    list_display = (
        "fullName",
        "phone",
        "department",
        "position",
        "formatted_start_date",
    )
    list_filter = ("department", "position")

    def formatted_start_date(self, obj):
        return obj.startDate.strftime("%d/%m/%Y") if obj.startDate else "-"

    formatted_start_date.short_description = "Ngày vào làm"


admin.site.register(NhanVien, NhanVienAdmin)
