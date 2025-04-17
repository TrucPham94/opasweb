from django.shortcuts import render, get_object_or_404
from .models import NganhHang, SanPham, AboutUs, ThongBao


def index(request):
    nganh_hang_list = NganhHang.objects.filter(status=True).order_by("name")
    anouncement_list = (
        ThongBao.objects.all().order_by("-ngay_dang").filter(loai_bai_viet="thongbao")
    )

    apply_memos = (
        ThongBao.objects.all().order_by("-ngay_dang").filter(loai_bai_viet="tuyendung")
    )

    return render(
        request,
        "index.html",
        {
            "nganh_hang_list": nganh_hang_list,
            "anouncement_list": anouncement_list,
            "apply_memos": apply_memos,
        },
    )


def about_us_view(request):
    about = AboutUs.objects.all()
    return render(request, "about-us.html", {"about": about})


def group(request):
    nganh_hang_list = NganhHang.objects.filter(status=True).order_by(
        "name"
    )  # chỉ lấy ngành đang hoạt động

    san_pham_list = SanPham.objects.filter(status=True)

    return render(
        request,
        "group.html",
        {
            "nganh_hang_list": nganh_hang_list,
            "san_pham_list": san_pham_list,
        },
    )


def apply(request):
    apply_memos = (
        ThongBao.objects.all().order_by("-ngay_dang").filter(loai_bai_viet="tuyendung")
    )
    return render(request, "apply.html", {"apply_memos": apply_memos})


def notifications(request):
    # Lấy danh sách thông báo từ cơ sở dữ liệu
    notifications = (
        ThongBao.objects.all().order_by("-ngay_dang").filter(loai_bai_viet="thongbao")
    )
    return render(request, "notifications.html", {"notifications": notifications})


def thong_bao_chi_tiet(request, pk):
    thong_bao = get_object_or_404(ThongBao, pk=pk)
    return render(request, "notifications_post.html", {"thong_bao": thong_bao})


def tin_tuyen_dung_chi_tiet(request, pk):
    post = get_object_or_404(ThongBao, pk=pk, loai_bai_viet="tuyendung")
    return render(request, "apply_post.html", {"tuyen_dung": post})
