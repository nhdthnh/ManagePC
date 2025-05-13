import subprocess
import platform

def is_computer_online(ip_address):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', ip_address]
    
    response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return response.returncode == 0

def is_online(ip_address):
    if (is_computer_online(ip_address)):
        return 'Online'
    else:
        return 'Offline'

