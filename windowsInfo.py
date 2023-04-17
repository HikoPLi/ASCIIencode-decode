import wmi
import json


local = wmi.WMI()


def cpuInfo():
    cpu = []
    cp = local.Win32_Processor()
    for info in cp:
        cpu.append(
            {
                "Name": info.Name,
                "Serial Number": info.Processorld,
                "CoreNum": info.NumberOfCores
            }
        )
    return cpu


# disk info


def getDiskInfo():
    disk = []
    for pd in local.Win32_DiskDrive():
        disk.append(
            {
                # 获取硬盘序列号，调用另外一个win32 API
                "Serial": local.Win32_PhysicalMedia()[0].SerialNumber.lstrip().rstrip(),
                "ID": pd.deviceid,
                "Caption": pd.Caption,
                "size": str(int(float(pd.Size)/1024/1024/1024))+"G"
            }
        )
    return disk

# mac location（include vitrual machine）


def getNetworkInfo():
    network = []
    for nw in local.Win32_NetworkAdapterConfiguration():  # IPEnabled=0
        if nw.MACAddress != None:
            network.append(
                {
                    "MAC": nw.MACAddress,  # 无线局域网适配器 WLAN 物理地址
                    "ip": nw.IPAddress
                }
            )
    return network

# Mainboard info


def getMainboardInfo():
    mainboard = []
    for board_id in local.Win32_BaseBoard():
        mainboard.append(board_id.SerialNumber.strip().strip('.'))
    return mainboard


def info():
    Info = [
        {
            "CPU_INFO": cpuInfo(),
            "DISK_INFO": getDiskInfo(),
            "NETWORK_INFO": getNetworkInfo(),
            "MAINBOARD_INFO": getMainboardInfo()
        }
    ]

    print(Info)

    with open("INFO.json", "w") as infoFile:
        info = json.dumps(Info)
        infoFile.write(info, sort_keys=True, indent=4)
        
    return Info
