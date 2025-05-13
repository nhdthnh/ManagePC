import COMPUTER_NAME
import CPU
import RAM
import IP
import MAC
import ONLINE


name = COMPUTER_NAME.name()
cpu = CPU.get_cpu_name()
ram_total = RAM.ram_total
ram_used = RAM.ram_used
ram_percent = RAM.ram_percent
ip = IP.get_ip_address()
mac = MAC.get_mac_address()
is_online = ONLINE.is_online(ip)