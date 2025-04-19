# hr/views.py

from django.shortcuts import render, redirect
from .forms import NhanVienForm


def index(request):
    return render(request, "hr/index.html")


def nhap_nhan_vien(request):
    if request.method == "POST":
        form = NhanVienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = NhanVienForm()
    return render(request, "hr/nhap_nhan_vien.html", {"form": form})
