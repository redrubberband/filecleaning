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

WheelUp::
Send {PgUp}
Send ^w
 ; sleep 1000
sleep 250
return

WheelDown::
Send {Right}
sleep, 600
 ; Send {PgDn}
return

1::ExitApp