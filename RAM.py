import psutil

ram_total = round(psutil.virtual_memory().total / (1024**3), 1)
ram_used = psutil.virtual_memory().used / (1024**3)
ram_used = round(ram_used, 1)
ram_percent = psutil.virtual_memory().percent
