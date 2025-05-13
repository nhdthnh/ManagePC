import winreg

def get_cpu_name():
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                      r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
        cpu_name, _ = winreg.QueryValueEx(registry_key, "ProcessorNameString")
        winreg.CloseKey(registry_key)
        return cpu_name.strip()
    except WindowsError:
        return "Unknown CPU"