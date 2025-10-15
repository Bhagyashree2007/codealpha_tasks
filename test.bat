@echo off
REM Run the test suite for emotion recognition
echo.
echo ========================================
echo   EMOTION RECOGNITION TEST SUITE
echo ========================================
echo.

call venv\Scripts\activate.bat

python test.py

echo.
pause
