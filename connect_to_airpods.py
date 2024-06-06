import time
import threading
from socket import socket, AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM
from winreg import OpenKey, EnumKey, QueryValueEx, HKEY_LOCAL_MACHINE

# script to be called from AutoHotKey in the startup directory
# computer needs to be already paired with the AirPods
# press Ctrl + Shift + M at any time from desktop to run
# defaults to Stereo audio


REG_BTH_ADDRS = r"SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters\Devices"
CHANNEL = 1

# Find the MAC address of the AirPods
keys = OpenKey(HKEY_LOCAL_MACHINE, REG_BTH_ADDRS)
i, found = 0, False
while not found:
    try:
        subkey = EnumKey(keys, i)
        try:
            name = QueryValueEx(OpenKey(keys, subkey), "Name")
            name_decoded = name[0].decode("utf-8")
            if "AirPods" in name_decoded:
                found = True
                airpods_mac_addr = ":".join([subkey[j : j + 2] for j in range(0, len(subkey), 2)]).upper()
                print(f"Found AirPods: {name_decoded}, MAC address: {airpods_mac_addr}")
        except FileNotFoundError:
            pass  # doesn't have a Name attribute
        i += 1
    except OSError:
        print("Did not find AirPods in list of connected Bluetooth devices.")
        raise

# Connect to the AirPods
def connect_to_airpods(airpods_mac_addr: str):
    sock = socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM)
    try:
        sock.connect((airpods_mac_addr, CHANNEL))  # MAC address, channel
    except OSError as e:
        if e.errno == 10051:  # network is unreachable
            raise
        else:
            print("Success - audio connection will begin within 30 seconds.")
            time.sleep(3)
    finally:
        sock.close()


thread = threading.Thread(target=connect_to_airpods, args=(airpods_mac_addr,), daemon=True)
thread.start()
thread.join(10)  # wait for 10 seconds
if thread.is_alive():
    print("Connection to AirPods timed out.")
