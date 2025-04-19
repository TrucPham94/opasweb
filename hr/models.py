from django.db import models

# Create your models here.


class NhanVien(models.Model):
    ho_ten = models.CharField(max_length=100)
    email = models.EmailField()
    phong_ban = models.CharField(max_length=100)
    ngay_vao_lam = models.DateField()
