import psutil


ram = psutil.virtual_memory().percent
#psutil.swap_memory()
#psutil.cpu_count()
cpu = psutil.cpu_percent(interval=2)
tempo_ocioso = psutil.cpu_times().idle // 2160
batt = psutil.sensors_battery().percent
#psutil.boot_times()
#psutil.users()

print('\n\nSTATUS COMPUTER\n')
print("".center(25, "*"))
print("RAM USED", ram, "%", "\nCPU USED", cpu, "%", "\nTIME RELAX", tempo_ocioso, "hrs", "\nBATTERY", batt, "%")
print("".center(25, "*"))
print('\n\n')

for proc in psutil.process_iter():
        if proc.pid == 871:
            print(proc.as_dict(["cpu_percent", "cpu_times"]))
        else:
            pass;