; Run from startup folder
; C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\connect_to_airpods.ahk

^+m::  ; Ctrl + Shift + M
	{
        ScriptPath := "C:\Users\lnick\Documents\Programming\Projects\Connect2Airpods\connect_to_airpods.py"
        Timeout := 10  ; seconds to allow bluetooth connection attempt
        RunWait("python " ScriptPath " --timeout " Timeout)
        return
    }
