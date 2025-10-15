# 🎤 How to Run and Test - Fixed Version

## ✅ All Errors Fixed!

The dependencies have been installed and the project is ready to use.

---

## 🚀 Three Easy Ways to Run

### **Method 1: Using Batch Files (EASIEST!)**

We've created simple `.bat` files for you:

#### Train the model:
```cmd
train.bat
```

#### Predict emotion:
```cmd
predict.bat
```
or
```cmd
predict.bat your_audio.wav
```

#### Run tests:
```cmd
test.bat
```

#### Interactive menu:
```cmd
run.bat
```

---

### **Method 2: Direct Python Commands**

#### 1. Train the model (first time only, takes 15-30 min):
```cmd
venv\Scripts\activate
python train.py
```

#### 2. Predict emotion from audio:
```cmd
venv\Scripts\activate
python predict.py sample.wav
```

#### 3. Run comprehensive tests:
```cmd
venv\Scripts\activate
python test.py
```

---

### **Method 3: Interactive Menu**

Double-click `run.bat` or run:
```cmd
run.bat
```

You'll get a menu:
```
========================================
  MAIN MENU
========================================
1. Train model
2. Predict emotion from sample.wav
3. Predict emotion from custom audio
4. Run test suite
5. View project info
6. Exit
```

---

## 📊 Expected Output

### Training (train.bat):
```
Loading tess dataset from TESS/...
Processing tess files: 100%|████████| 2800/2800
Loading cremad dataset from CREMA-D/...
Processing cremad files: 100%|████████| 7442/7442
Training model... Done
Test Accuracy: 0.75
```

### Prediction (predict.bat):
```
Predicted Emotions with Confidence:

Happy: 76.61%
Angry: 6.42%
Disgust: 6.35%
Neutral: 6.04%
Sad: 2.41%
Fear: 2.17%
```

### Testing (test.bat):
```
========================================
Testing on TESS dataset
========================================
Testing: 100%|████████| 50/50

Classification Report:
              precision    recall  f1-score   support

       Angry       0.85      0.82      0.83        50
       ...

Overall Accuracy: 77.00%

Confusion matrix saved as 'confusion_matrix_tess.png'
```

---

## 🎯 Quick Start Guide

### If model is NOT trained yet:
```cmd
REM 1. Train model (one time, 15-30 minutes)
train.bat

REM 2. Test it works
predict.bat

REM 3. Run full evaluation
test.bat
```

### If model IS already trained:
```cmd
REM Quick prediction
predict.bat

REM Or custom file
predict.bat "path\to\your\audio.wav"

REM Full testing
test.bat
```

---

## 📁 All Available Commands

| Command | What it does | Time |
|---------|--------------|------|
| `train.bat` | Train the model | 15-30 min |
| `predict.bat` | Predict from sample.wav | 2 sec |
| `predict.bat file.wav` | Predict from your file | 2 sec |
| `test.bat` | Run full test suite | 2-5 min |
| `run.bat` | Interactive menu | - |

---

## 🔧 Troubleshooting

### Problem: "Model not trained"
**Solution:**
```cmd
train.bat
```

### Problem: "File not found"
**Solution:** Use full path with quotes:
```cmd
predict.bat "C:\path\to\audio.wav"
```

### Problem: Batch file doesn't run
**Solution:** Right-click → "Run as administrator"

### Problem: Virtual environment errors
**Solution:**
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 💡 Tips

1. **First time?** Run `train.bat` first
2. **Quick test?** Run `predict.bat`
3. **Full evaluation?** Run `test.bat`
4. **Easy menu?** Run `run.bat`

---

## ✅ What's Fixed

- ✅ All dependencies installed (lightgbm, librosa, matplotlib, etc.)
- ✅ Virtual environment configured
- ✅ Simple batch files created
- ✅ PowerShell script issues resolved
- ✅ Test suite ready to use

---

## 🎉 You're Ready!

**Quickest way to start:**
```cmd
train.bat
```

Then:
```cmd
predict.bat
```

**Happy Testing! 🚀**
