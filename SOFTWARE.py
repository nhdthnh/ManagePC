import winreg

def list_installed_programs():
    uninstall_key = r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall'
    programs = []

    for root in [winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE]:
        try:
            registry_key = winreg.OpenKey(root, uninstall_key)
            for i in range(winreg.QueryInfoKey(registry_key)[0]):
                sub_key_name = winreg.EnumKey(registry_key, i)
                sub_key = winreg.OpenKey(registry_key, sub_key_name)
                try:
                    program_name = winreg.QueryValueEx(sub_key, 'DisplayName')[0]
                    programs.append(program_name)
                except FileNotFoundError:
                    pass
        except Exception as e:
            pass

    for program in sorted(programs):
        print(program)

# Sử dụng hàm
list_installed_programs()
