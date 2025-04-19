
# ✅ To-Do List: Dự án Website Công Ty với Django (Quản Lý Nhân Sự)

## Giai đoạn 1: Chuẩn bị
- [ ] Tạo project Django: `company_website`
- [ ] Cài đặt database (MySQL hoặc PostgreSQL)
- [ ] Cấu hình `settings.py` (STATIC, MEDIA, DATABASE, TIME_ZONE)
- [ ] Tạo app chính: `nhansu` (hoặc `hrm`)
- [ ] Tạo app: `pages` (giới thiệu, tin tức, liên hệ,...)

## Giai đoạn 2: Quản lý nhân sự
- [ ] Thiết kế models:
  - [ ] `NhanVien` (Tên, ngày sinh, giới tính, phòng ban, chức vụ…)
  - [ ] `PhongBan` (Tên phòng, mô tả)
  - [ ] `ChucVu` (Tên chức vụ)
  - [ ] `HopDong` (Loại hợp đồng, thời hạn, ngày ký…)
- [ ] Đăng ký các model vào admin
- [ ] Tạo trang CRUD cơ bản (danh sách, thêm, sửa, xóa)
- [ ] Thêm tìm kiếm + filter trong admin

## Giai đoạn 3: Báo cáo & biểu đồ
- [ ] Tích hợp Chart.js để:
  - [ ] Thống kê số lượng nhân viên theo phòng ban
  - [ ] Thống kê nhân viên theo giới tính
  - [ ] (Tuỳ chọn) Biểu đồ lương theo tháng

## Giai đoạn 4: Xuất dữ liệu & báo cáo
- [ ] Xuất danh sách nhân viên ra Excel
- [ ] Xuất hợp đồng ra PDF
- [ ] Gửi email thông báo hợp đồng sắp hết hạn (nâng cao)

## Giai đoạn 5: Website chính
- [ ] Tạo trang chủ công ty (`pages`)
- [ ] Tạo trang giới thiệu, dịch vụ, liên hệ
- [ ] Tích hợp TinyMCE để viết bài blog/tin tức
- [ ] Tích hợp contact form gửi về email

## Giai đoạn cuối: Hoàn thiện & triển khai
- [ ] Thêm Bootstrap 5 cho giao diện thân thiện
- [ ] Xử lý phân quyền: chỉ admin mới được sửa nhân sự
- [ ] Triển khai lên hosting (PythonAnywhere, VPS,…)
- [ ] Backup database + media định kỳ



<!-- Cần làm -->
gắn url từ bài viết trang index
