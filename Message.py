import socket

def receive_message():
    port = 12345  # Phải khớp với cổng của máy chủ
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", port))  # Lắng nghe trên tất cả các IP
    
    print("Đang chờ tin nhắn...")
    while True:
        data, addr = sock.recvfrom(1024)  # Nhận dữ liệu
        message = data.decode()
        print(f"Tin nhắn từ {addr[0]}: {message}")

# Chạy để lắng nghe tin nhắn từ máy chủ
receive_message()
