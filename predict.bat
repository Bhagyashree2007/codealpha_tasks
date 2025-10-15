@echo off
REM Quick prediction script for Speech Emotion Recognition
echo.
echo Starting prediction...
echo.

call venv\Scripts\activate.bat

if "%1"=="" (
    REM No argument provided, use sample.wav
    if exist sample.wav (
        python predict.py sample.wav
    ) else (
        echo ERROR: sample.wav not found!
        echo.
        echo Usage: predict.bat [audio-file.wav]
        echo Example: predict.bat sample.wav
    )
) else (
    REM Use the provided file
    if exist "%1" (
        python predict.py "%1"
    ) else (
        echo ERROR: File not found: %1
    )
)

echo.
pause
