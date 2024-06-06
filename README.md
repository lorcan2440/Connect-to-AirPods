# Connect-to-AirPods

Automatically connects paired Apple AirPods to a Windows computer via Bluetooth. Uses only built-in Python modules.
The Python script `connect_to_airpods.py` can be run on its own to connect, or called from [AutoHotKey 2](https://www.autohotkey.com/v2/) via the script `connect_to_airpods.ahk` to automatically connect when a keyboard shortcut is pressed.

## Requirements
- OS: Windows 10 or 11
- Python: 3.11
- AutoHotKey: 2.0

## How to run

1. Save the two scripts `connect_to_airpods.py` and `connect_to_airpods.ahk` somewhere on your computer.
2. Create a shortcut to `connect_to_airpods.ahk` and move it to the Windows startup folder: `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\`
3. Edit the file `connect_to_airpods.ahk` and change the path in the `ScriptPath` variable to the full path of the Python script `connect_to_airpods.py` and save.
4. Restart your computer and once back, check the AutoHotKey script is running by going to the system tray, right-click the green 'H' icon, Open, and see if `connect_to_airpods.ahk` has returned.
5. With your AirPods in your ears, to connect your AirPods, press `Ctrl + Shift + M`.

Afterwards, you can just do Step 5 at any time.

## Notes

To change the keyboard shortcut, edit the code in `connect_to_airpods.ahk` before the `::`, currently set to `^+m` which represents Ctrl (^), Shift (+), M (m). Use the table [here](https://www.autohotkey.com/docs/v2/Hotkeys.htm#Symbols) to change it. Save and restart/run manually.

The connection can take up to 30 seconds and the time can vary. On my device, it takes ~5 seconds for the AirPods to 'ping', and then audio playback starts after another ~10 seconds. Sound defaults to Stereo audio.
