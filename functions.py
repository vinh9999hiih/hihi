import requests

def find_admin_page(base_url):
    """
    Tìm trang admin của một website bằng cách thử các đường dẫn phổ biến.
    :param base_url: Địa chỉ cơ sở của website (ví dụ: "http://bun.sub").
    :return: Đường dẫn đến trang admin nếu tìm thấy, ngược lại trả về None.
    """
    # Danh sách các đường dẫn admin phổ biến
    admin_paths = [
        "/admin",
        "/admin/login",
        "/adminpanel",
        "/wp-admin",
        "/wp-login.php",
        "/administrator",
        "/login",
        "/manager",
        "/admin.php",
        "/admin/index.php",
        "/admin_area",
        "/admin1",
        "/admin2",
        "/admin3",
        "/admin4",
        "/admin5",
    ]

    # Thử từng đường dẫn
    for path in admin_paths:
        url = base_url + path
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:  # Trang tồn tại
                print(f"Tìm thấy trang admin tại: {url}")
                return url
        except requests.RequestException as e:
            print(f"Lỗi khi truy cập {url}: {e}")

    print("Không tìm thấy trang admin.")
    return None


# Ví dụ sử dụng
if __name__ == "__main__":
    base_url = "http://bun.sub"  # Thay bằng địa chỉ website bạn muốn kiểm tra
    admin_page = find_admin_page(base_url)
    if admin_page:
        print(f"Trang admin được tìm thấy: {admin_page}")
    else:
        print("Không tìm thấy trang admin.")
