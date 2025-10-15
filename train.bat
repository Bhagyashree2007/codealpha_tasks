@echo off
REM Train the emotion recognition model
echo.
echo ========================================
echo   TRAINING EMOTION RECOGNITION MODEL
echo ========================================
echo.
echo This will take 15-30 minutes depending on your CPU.
echo The model will be trained on TESS and CREMA-D datasets.
echo.

call venv\Scripts\activate.bat

python train.py

echo.
echo ========================================
echo   TRAINING COMPLETE!
echo ========================================
echo.
pause
