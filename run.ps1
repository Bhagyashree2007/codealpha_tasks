# Speech Emotion Recognition - Run Script
# This script helps you easily train and test the model

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  SPEECH EMOTION RECOGNITION" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Check if virtual environment exists
if (Test-Path "venv") {
    Write-Host "✓ Virtual environment found" -ForegroundColor Green
    Write-Host "  Activating virtual environment...`n" -ForegroundColor Yellow
    & ".\venv\Scripts\Activate.ps1"
} else {
    Write-Host "! Virtual environment not found" -ForegroundColor Yellow
    $create = Read-Host "  Create virtual environment? (y/n)"
    if ($create -eq 'y') {
        Write-Host "`nCreating virtual environment..." -ForegroundColor Yellow
        python -m venv venv
        & ".\venv\Scripts\Activate.ps1"
        Write-Host "✓ Virtual environment created`n" -ForegroundColor Green
    }
}

# Check if dependencies are installed
Write-Host "Checking dependencies..." -ForegroundColor Yellow
$hasLibrosa = python -c "import librosa" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "! Dependencies not installed" -ForegroundColor Yellow
    $install = Read-Host "  Install dependencies? (y/n)"
    if ($install -eq 'y') {
        Write-Host "`nInstalling dependencies..." -ForegroundColor Yellow
        pip install -r requirements.txt
        Write-Host "✓ Dependencies installed`n" -ForegroundColor Green
    }
} else {
    Write-Host "✓ Dependencies installed`n" -ForegroundColor Green
}

# Check if model is trained
$modelExists = Test-Path "model.pkl"
$encoderExists = Test-Path "label_encoder.pkl"

if (-not $modelExists -or -not $encoderExists) {
    Write-Host "! Model not trained yet" -ForegroundColor Yellow
    Write-Host "`nYou need to train the model first." -ForegroundColor Yellow
    $train = Read-Host "  Start training now? (y/n)"
    if ($train -eq 'y') {
        Write-Host "`nStarting training..." -ForegroundColor Yellow
        Write-Host "This may take 15-30 minutes depending on your CPU`n" -ForegroundColor Cyan
        python train.py
        Write-Host "`n✓ Training complete!`n" -ForegroundColor Green
    } else {
        Write-Host "`nPlease run 'python train.py' to train the model first.`n" -ForegroundColor Red
        exit
    }
} else {
    Write-Host "✓ Model is trained`n" -ForegroundColor Green
}

# Main menu
while ($true) {
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "  MAIN MENU" -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "1. Predict emotion from sample.wav" -ForegroundColor White
    Write-Host "2. Predict emotion from custom audio file" -ForegroundColor White
    Write-Host "3. Run test suite (interactive)" -ForegroundColor White
    Write-Host "4. Retrain model" -ForegroundColor White
    Write-Host "5. View project info" -ForegroundColor White
    Write-Host "6. Exit" -ForegroundColor White
    Write-Host "========================================`n" -ForegroundColor Cyan
    
    $choice = Read-Host "Enter your choice (1-6)"
    
    switch ($choice) {
        "1" {
            Write-Host "`n" -NoNewline
            if (Test-Path "sample.wav") {
                python predict.py sample.wav
            } else {
                Write-Host "✗ sample.wav not found!" -ForegroundColor Red
            }
            Write-Host "`n"
            Read-Host "Press Enter to continue..."
        }
        "2" {
            $audioFile = Read-Host "`nEnter path to audio file"
            if (Test-Path $audioFile) {
                Write-Host "`n" -NoNewline
                python predict.py $audioFile
            } else {
                Write-Host "✗ File not found: $audioFile" -ForegroundColor Red
            }
            Write-Host "`n"
            Read-Host "Press Enter to continue..."
        }
        "3" {
            Write-Host "`n" -NoNewline
            python test.py
            Write-Host "`n"
            Read-Host "Press Enter to continue..."
        }
        "4" {
            Write-Host "`n" -NoNewline
            $confirm = Read-Host "This will retrain the model. Continue? (y/n)"
            if ($confirm -eq 'y') {
                Write-Host "`nRetraining model..." -ForegroundColor Yellow
                python train.py
                Write-Host "`n✓ Retraining complete!" -ForegroundColor Green
            }
            Write-Host "`n"
            Read-Host "Press Enter to continue..."
        }
        "5" {
            Write-Host "`n========================================" -ForegroundColor Cyan
            Write-Host "  PROJECT INFO" -ForegroundColor Cyan
            Write-Host "========================================" -ForegroundColor Cyan
            Write-Host "Model Status:" -ForegroundColor Yellow
            if (Test-Path "model.pkl") {
                $modelSize = (Get-Item "model.pkl").Length / 1MB
                Write-Host "  ✓ Model trained (${modelSize:N2} MB)" -ForegroundColor Green
            } else {
                Write-Host "  ✗ Model not trained" -ForegroundColor Red
            }
            
            Write-Host "`nDatasets:" -ForegroundColor Yellow
            if (Test-Path "CREMA-D") {
                $cremadCount = (Get-ChildItem -Recurse "CREMA-D" -File).Count
                Write-Host "  ✓ CREMA-D: $cremadCount files" -ForegroundColor Green
            } else {
                Write-Host "  ✗ CREMA-D: Not found" -ForegroundColor Red
            }
            
            if (Test-Path "TESS") {
                $tessCount = (Get-ChildItem -Recurse "TESS" -File).Count
                Write-Host "  ✓ TESS: $tessCount files" -ForegroundColor Green
            } else {
                Write-Host "  ✗ TESS: Not found" -ForegroundColor Red
            }
            
            Write-Host "`nPython Environment:" -ForegroundColor Yellow
            python --version
            
            Write-Host "`n========================================`n" -ForegroundColor Cyan
            Read-Host "Press Enter to continue..."
        }
        "6" {
            Write-Host "`nGoodbye! 👋`n" -ForegroundColor Cyan
            exit
        }
        default {
            Write-Host "`n✗ Invalid choice. Please enter 1-6.`n" -ForegroundColor Red
        }
    }
    
    Clear-Host
}
