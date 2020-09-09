#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance force

RButton::
Send v
sleep, 250
send x
sleep, 250
 ; Click, right
return

~MButton & RButton::
Click, right
return

WheelUp::
Send {PgUp}
Send ^w
 ; sleep 1000
sleep 250
return

~MButton & WheelUp::
Send ^c
sleep, 600
return

~MButton & WheelDown::
Send ^v
Click, right
sleep, 600
return

WheelDown::
Send {PgDn}
Send {Right}
sleep, 600
return

~LButton & RButton::
Send {PgDn}
return

1::ExitApp