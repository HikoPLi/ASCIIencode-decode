import platform
import psutil
import json


def info():

    Info = [
        {
            "Computer network names": f"{platform.node()}",  # -> element 1
            "Machine type": f"{platform.machine()}",
            "Processor type": f"{platform.processor()}",
            "Platform type": f"{platform.platform()}",
            "Operating system": f"{platform.system()}",
            "Operating system release": f"{platform.release()}",
            # -> elements 2
            "Operating system version": f"{platform.version()}",
            # -> element 3
            "Number of physical cores": f"{psutil.cpu_count(logical=False)}",
            # -> element 4
            "Number of logical cores": f"{psutil.cpu_count(logical=True)}",
            # -> element 5
            "Current CPU utilization": f"{psutil.cpu_percent(interval=1)}",
            # -> elements 6
            "Current per-CPU utilization": f"{psutil.cpu_percent(interval=1, percpu=True)}",
            "Total RAM installed": f"{round(psutil.virtual_memory().total/1000000000, 2)} GB",
            "Available RAM": f"{round(psutil.virtual_memory().available/1000000000, 2)} GB",
            "Used RAM": f"{round(psutil.virtual_memory().used/1000000000, 2)} GB",
            "RAM usage": f"{psutil.virtual_memory().percent}%"
        }
    ]

    print(Info)
    elements = f"{platform.node()}{platform.release()}{platform.version()}{psutil.cpu_count(logical=False)}{psutil.cpu_count(logical=True)}{psutil.cpu_percent(interval=1)}"
    with open("INFO.json", "w") as infoFile:
        info = json.dumps(Info)
        infoFile.write(info)

    return elements
