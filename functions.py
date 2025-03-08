import requests
from urllib3.exceptions import InsecureRequestWarning
import sys
import io

# Tắt cảnh báo SSL không an toàn (nếu cần)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Đặt encoding mặc định cho stdin và stdout
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


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
            # Gửi yêu cầu GET với SSL verify=False (nếu cần)
            response = requests.get(url, timeout=5, verify=False)
            if response.status_code == 200:  # Trang tồn tại
                print(f"Tìm thấy trang admin tại: {url}")
                return url
        except requests.exceptions.RequestException as e:
            print(f"Lỗi khi truy cập {url}: {e}")

    print("Không tìm thấy trang admin.")
    return None


# Ví dụ sử dụng
if __name__ == "__main__":
    try:
        # Nhập địa chỉ website từ người dùng
        base_url = input("Nhập địa chỉ website (ví dụ: http://bun.sub): ").strip()
        if not base_url.startswith(("http://", "https://")):
            base_url = "http://" + base_url  # Mặc định sử dụng HTTP nếu không có scheme

        # Tìm trang admin
        admin_page = find_admin_page(base_url)
        if admin_page:
            print(f"Trang admin được tìm thấy: {admin_page}")
        else:
            print("Không tìm thấy trang admin.")
    except Exception as e:
        print(f"Lỗi: {e}")
