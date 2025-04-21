from django.db import models


class NhanVien(models.Model):
    GENDER_CHOICES = [
        ("Nam", "Nam"),
        ("Nữ", "Nữ"),
        ("Khác", "Khác"),
    ]

    PHONG_BAN_CHOICES = [
        ("Phòng Kế toán", "Phòng Kế toán"),
        ("Hành chính Nhân sự", "Hành chính Nhân sự"),
        ("Kinh doanh", "Kinh doanh"),
        ("Điều vận", "Điều vận"),
    ]

    fullName = models.CharField(
        max_length=100, default="Họ tên đầy đủ", verbose_name="Họ tên"
    )
    idNumber = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField(verbose_name="Ngày sinh")
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, verbose_name="Giới tính"
    )
    department = models.CharField(
        max_length=50, choices=PHONG_BAN_CHOICES, verbose_name="Phòng ban"
    )
    position = models.CharField(max_length=50, verbose_name="Vị trí")
    address = models.TextField(blank=True, verbose_name="Địa chỉ")
    startDate = models.DateField(verbose_name="Ngày vào làm")
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.fullName
