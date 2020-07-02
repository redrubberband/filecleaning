@echo off

set "filtro=%1"
if [%filtro%]==[] (
    set "filtro=*.mp4"
    )

for /R %%a in (%filtro%) do call :doWork "%%a"

    REM PAUSE
    ECHO "==========================================" >> log.txt
    exit /B

:doWork
	REM -i means input
	REM -af is audiofilter
	REM -vn is... idk from ffmpeg itself
	REM -f null means the output is null, ffmpeg itself does not generate work
	REM %1 is the current filename
	REM and please do not do anything to this file outside the doWork, I copied it from 
	REM https://stackoverflow.com/questions/51440630/how-to-find-if-the-videos-have-sound-in-it
	REM https://superuser.com/questions/100288/how-can-i-check-the-integrity-of-a-video-file-avi-mpeg-mp4
    ffmpeg -hide_banner -i %1 -af volumedetect -vn -f null - 2>&1 | findstr mean_volume >> log.txt
    ECHO %1 >> log.txt