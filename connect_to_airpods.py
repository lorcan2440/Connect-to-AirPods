import time
import socket
import winreg

# script to be called from AutoHotKey in the startup directory
# computer needs to be already paired with the AirPods
# press Ctrl + Shift + M at any time from desktop to run
# defaults to Stereo audio


REG_BTH_ADDRS = r'SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters\Devices'
CHANNEL = 1

# Find the MAC address of the AirPods
keys = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_BTH_ADDRS)
i, found = 0, False
while not found:
    try:
        subkey = winreg.EnumKey(keys, i)
        try:
            name = winreg.QueryValueEx(winreg.OpenKey(keys, subkey), 'Name')
            if 'AirPods' in name[0].decode('utf-8'):
                found = True
                airpods_mac_addr = ':'.join([subkey[j:j + 2] for j in range(0, len(subkey), 2)]).upper()
                print(f'Found AirPods with MAC address: {airpods_mac_addr}')
                break
        except FileNotFoundError:
            pass  # doesn't have a Name attribute
        i += 1
    except OSError:
        print('Did not find AirPods in list of connected Bluetooth devices.')
        raise

# Connect to the AirPods
sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
try:
    sock.connect((airpods_mac_addr, CHANNEL))  # MAC address, channel
except OSError as e:
    if e.errno == 10051:  # network is unreachable
        raise
    else:
        print('Success - audio connection will begin within 30 seconds.')
        time.sleep(3)
finally:
    sock.close()
