# forms.py
from django import forms
from .models import NhanVien


class NhanVienForm(forms.ModelForm):
    class Meta:
        model = NhanVien
        fields = "__all__"
