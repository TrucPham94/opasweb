# hr/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import NhanVienForm
from .models import NhanVien
from .forms import NhanVienForm
import openpyxl
from django.http import HttpResponse
from django.db.models import Count


def index(request):
    return render(request, "hr/index.html")


# hàm tải excel về


def export_nhan_vien_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Danh sách nhân viên"

    # Header
    headers = [
        "Họ và tên",
        "Căn cước công dân",
        "Email",
        "Điện thoại",
        "Ngày sinh",
        "Giới tính",
        "Phòng ban",
        "Chức vụ",
        "Địa chỉ",
        "Ngày vào làm",
        "Ghi chú",
    ]
    ws.append(headers)

    # Dữ liệu
    for nv in NhanVien.objects.all():
        ws.append(
            [
                nv.fullName,
                nv.idNumber,
                nv.email,
                nv.phone,
                nv.dob.strftime("%d/%m/%Y") if nv.dob else "",
                nv.gender,
                nv.department,
                nv.position,
                nv.address,
                nv.startDate.strftime("%d/%m/%Y") if nv.startDate else "",
                nv.notes,
            ]
        )

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = "attachment; filename=DanhSachNhanVien.xlsx"
    wb.save(response)
    return response


def nhap_nhan_vien(request):
    if request.method == "POST":
        form = NhanVienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "danh_sach_nhan_vien"
            )  # Hoặc redirect tới một trang bạn muốn
    else:
        form = NhanVienForm()
    return render(request, "hr/nhap_nhan_vien.html", {"form": form})


def danh_sach_nhan_vien(request):
    nhan_vien_list = NhanVien.objects.all().order_by("-id")
    return render(
        request,
        "hr/danh_sach_nhan_vien.html",
        {
            "nhan_vien_list": nhan_vien_list,
        },
    )


# profile


def profile_nhan_vien(request, pk):
    nhan_vien = get_object_or_404(NhanVien, pk=pk)
    return render(request, "hr/profile_nhan_vien.html", {"nhan_vien": nhan_vien})


def bao_cao_nhan_su(request):
    thong_ke = (
        NhanVien.objects.values("department")
        .annotate(tong=Count("id"))
        .order_by("-tong")
    )

    labels = [item["department"] for item in thong_ke]
    data = [item["tong"] for item in thong_ke]

    return render(
        request,
        "hr/bao_cao_nhan_su.html",
        {
            "labels": labels,
            "data": data,
            "thong_ke": thong_ke,
        },
    )


def profile_nhan_vien(request, pk):
    nhan_vien = get_object_or_404(NhanVien, pk=pk)
    return render(request, "hr/profile_nhan_vien.html", {"nhan_vien": nhan_vien})
