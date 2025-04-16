from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from .function import RenameFileImage


class NganhHang(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    fullname = models.CharField(max_length=200)
    introduce = RichTextUploadingField(blank=True)
    logo = models.ImageField(
        upload_to=RenameFileImage("logo-nganh-hang", "name"), blank=True, null=True
    )
    status = models.BooleanField(default=True, verbose_name="Còn hoạt động")
    ngay_bat_dau = models.DateField(verbose_name="Ngày bắt đầu hoạt động")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ngành hàng"
        verbose_name_plural = "Ngành hàng"


# Product
class SanPham(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=True, verbose_name="Còn hoạt động")
    hinh_anh = models.ImageField(
        upload_to=RenameFileImage("anh_san_pham", "name"), blank=True, null=True
    )
    # Liên kết tới ngành hàng
    nganh_hang = models.ForeignKey(
        NganhHang, on_delete=models.CASCADE, related_name="san_pham_list"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sản phẩm"
        verbose_name_plural = "Sản phẩm"


# About Us
class AboutUs(models.Model):
    title = models.CharField(
        max_length=200, default="tiêu đề mới", verbose_name="Tiêu đề"
    )

    content = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Giới thiệu"
        verbose_name_plural = "Giới thiệu"


# Thông báo
class ThongBao(models.Model):
    LOAI_CHOICES = [
        ("thongbao", "Thông báo"),
        ("tuyendung", "Tuyển dụng"),
    ]

    tieu_de = models.CharField(max_length=255, verbose_name="Tiêu đề")
    noi_dung = RichTextUploadingField(verbose_name="Nội dung", blank=True)
    ngay_dang = models.DateTimeField(auto_now_add=True, verbose_name="Ngày đăng")
    hien_thi = models.BooleanField(default=True, verbose_name="Hiển thị")
    thumbnail = models.ImageField(
        upload_to=RenameFileImage("thong_bao", "tieu_de"), blank=True, null=True
    )

    tep_dinh_kem = models.FileField(
        upload_to="thong_bao/files/", blank=True, null=True, verbose_name="Tệp đính kèm"
    )

    loai_bai_viet = models.CharField(
        max_length=20,
        choices=LOAI_CHOICES,
        default="thongbao",
        verbose_name="Loại bài viết",
    )

    def __str__(self):
        return self.tieu_de

    class Meta:
        verbose_name = "Thông báo"
        verbose_name_plural = "Thông báo"
        ordering = ["-ngay_dang"]  # Mới nhất lên đầu
