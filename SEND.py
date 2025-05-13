import socket

def send_message(target_ip, message):
    port = 12345  # Cổng mặc định cho giao tiếp
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Dùng UDP
    sock.sendto(message.encode(), (target_ip, port))
    sock.close()
    print(f"Đã gửi tin nhắn đến {target_ip}: {message}")

# Sử dụng
target_ip = "192.168.150.35"  # IP của máy đích
message = "XIN CHAO"
send_message(target_ip, message)
