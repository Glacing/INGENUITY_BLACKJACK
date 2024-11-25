setlocal EnableDelayedExpansion

:: Configuration

set BASE_PATH=.\

:: List of scripts to launch (relative to base path)
set SCRIPTS[0]=Gestionnaire\main.py
set SCRIPTS[1]=Joueur\main.py
set SCRIPTS[2]=Joueur\main.py
set SCRIPTS[3]=Pioche\main.py


:: Launch each script minimized
set /a SCRIPT_COUNT=3
for /L %%i in (0,1,%SCRIPT_COUNT%-1) do (
    if %%i==0 (
        echo Running Script 0
        start /B cmd /c "python3 "%BASE_PATH%!SCRIPTS[%%i]!" Gestionnaire Wi-Fi 5670"
    ) else if %%i==1 (
        echo Running Script 1
        start /B cmd /c "python3 "%BASE_PATH%!SCRIPTS[%%i]!" J1 Wi-Fi 5670"
    ) else if %%i==2 (
        echo Running Script 2
        start /B cmd /c "python3 "%BASE_PATH%!SCRIPTS[%%i]!" J2 Wi-Fi 5670"
    ) else if %%i==3 (
        echo Running Script 3
        start /B cmd /c "python3 "%BASE_PATH%!SCRIPTS[%%i]!" Pioche Wi-Fi 5670"
    ) else (
        echo Script %%i is not explicitly handled
        
    )
)

start "" "C:\Users\aurel\Downloads\Whiteboard.win64\Whiteboard\Whiteboard.exe"
echo All Ingescape scripts launched minimized


@echo off
echo Verification des processus Python en cours...s

if errorlevel 1 (
    echo Aucun processus Python n'est en cours d'exécution.
) else (
    echo Arrêt des processus Python...
    taskkill /F /IM python.exe /T
)

echo Fin de l'arrêt des processus.
pause