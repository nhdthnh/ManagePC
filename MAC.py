import uuid

def get_mac_address():
    mac = uuid.getnode()
    mac_address = ':'.join(['{:02x}'.format((mac >> ele) & 0xff)
                           for ele in range(40, -1, -8)])
    return mac_address
