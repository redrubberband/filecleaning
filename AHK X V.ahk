#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance force

;RButton::
;send {MButton}
;return

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
;Send {WheelUp}
Send {PgUp}
Send {Esc}
;Send {Left}
Send ^w
; sleep 1000
sleep 250
return

WheelDown::
;Send {PgDn}
Send {WheelDown}
;Send {Right}
;sleep, 100
return

~MButton & WheelUp::
Send ^c
Click, right
sleep, 600
return

~RButton & WheelUp::
Send {PgUp}
Send {Esc}
;Send {Left}
Send ^w
sleep 1000
;sleep 250
return

~LButton & RButton::
Send {Right}
;Send {Left}
return

~Shift & RButton::
Send {Shift down}{Click, right}
return

PrintScreen::
	Send \
	return
1::ExitApp