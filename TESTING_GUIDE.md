# 🎤 Complete Testing & Running Guide

## 🚀 Quick Start (3 Easy Steps)

### Method 1: Using the Interactive Script (Easiest!)

```powershell
# Run the interactive script
.\run.ps1
```

This will:
- ✅ Check and activate virtual environment
- ✅ Install dependencies if needed
- ✅ Train model if not trained
- ✅ Show interactive menu for all operations

### Method 2: Manual Step-by-Step

#### Step 1: Setup Environment
```powershell
# Install dependencies
pip install -r requirements.txt
```

#### Step 2: Train the Model
```powershell
python train.py
```
**Time:** 15-30 minutes  
**Output:** `model.pkl` and `label_encoder.pkl` files

#### Step 3: Test/Predict
```powershell
# Quick test on sample
python predict.py sample.wav

# Test your own file
python predict.py "path/to/your/audio.wav"

# Run full test suite
python test.py
```

---

## 📊 Testing Options Explained

### Option A: Single File Prediction
**Command:**
```powershell
python predict.py sample.wav
```

**Output:**
```
Predicted Emotions with Confidence:

Happy: 76.61%
Angry: 6.42%
Disgust: 6.35%
Neutral: 6.04%
Sad: 2.41%
Fear: 2.17%
```

**Use when:** You want to quickly check emotion of one audio file

---

### Option B: Interactive Test Suite
**Command:**
```powershell
python test.py
```

**What you get:**
```
🎤 SPEECH EMOTION RECOGNITION - TEST SUITE
============================================================
Select test option:
1. Test on sample.wav
2. Test on TESS dataset (sample)
3. Test on CREMA-D dataset (sample)
4. Test on custom audio file
5. Quick test on all datasets
```

**Features:**
- 📈 Classification reports (Precision, Recall, F1-score)
- 📊 Confusion matrix visualizations (saved as PNG)
- 🎯 Visual confidence bars
- 📉 Per-class performance metrics

**Use when:** You want detailed performance analysis

---

### Option C: PowerShell Interactive Menu
**Command:**
```powershell
.\run.ps1
```

**What you get:**
```
========================================
  MAIN MENU
========================================
1. Predict emotion from sample.wav
2. Predict emotion from custom audio file
3. Run test suite (interactive)
4. Retrain model
5. View project info
6. Exit
```

**Features:**
- 🔧 Automatic setup checking
- 📦 Dependency management
- 🎯 Easy navigation
- ℹ️ Project status overview

**Use when:** You want the easiest, all-in-one experience

---

## 🎯 What Each File Does

| File | Purpose | When to Use |
|------|---------|-------------|
| `train.py` | Trains the emotion recognition model | Once at start, or when retraining |
| `predict.py` | Predicts emotion from a single audio file | Quick predictions |
| `test.py` | Comprehensive testing with metrics | Detailed evaluation |
| `run.ps1` | Interactive menu for all operations | Easiest workflow |
| `extract.py` | Extracts audio features | Used internally |
| `dataset_loader.py` | Loads TESS/CREMA-D datasets | Used internally |

---

## 📈 Understanding Test Results

### 1. Classification Report Example
```
              precision    recall  f1-score   support

       Angry       0.85      0.82      0.83        50
     Disgust       0.78      0.75      0.76        45
        Fear       0.72      0.70      0.71        40
       Happy       0.88      0.90      0.89        55
     Neutral       0.65      0.68      0.66        42
         Sad       0.75      0.73      0.74        48

    accuracy                           0.77       280
```

**What it means:**
- **Precision:** How many predicted emotions were correct
- **Recall:** How many actual emotions were found
- **F1-score:** Balance between precision and recall
- **Support:** Number of test samples

### 2. Confusion Matrix
![Confusion Matrix Example](confusion_matrix_example.png)

Shows which emotions are confused with each other.

### 3. Confidence Scores
```
Happy: 76.61%    ████████████████████████████████████████
Angry: 6.42%     ███
Disgust: 6.35%   ███
```

**Interpretation:**
- **> 60%** = Strong prediction ✅
- **40-60%** = Moderate confidence ⚠️
- **< 40%** = Low confidence, ambiguous ❓

---

## 🔧 Common Workflows

### Workflow 1: First-Time Setup & Test
```powershell
# 1. Install
pip install -r requirements.txt

# 2. Train
python train.py

# 3. Quick test
python predict.py sample.wav

# 4. Full evaluation
python test.py
# Choose option 5
```

### Workflow 2: Test Your Own Audio
```powershell
# Record or prepare your audio file (WAV format recommended)

# Predict emotion
python predict.py "my_audio.wav"
```

### Workflow 3: Evaluate Model Performance
```powershell
# Run comprehensive tests
python test.py

# Select option 5: "Quick test on all datasets"

# Review results:
# - Console output shows metrics
# - PNG files saved with confusion matrices
```

### Workflow 4: Using the Easy Menu
```powershell
# Just run this and follow prompts
.\run.ps1
```

---

## 🎨 Output Files Generated

After running tests, you'll see:

| File | Description |
|------|-------------|
| `model.pkl` | Trained model (2-3 MB) |
| `label_encoder.pkl` | Emotion label encoder |
| `confusion_matrix_tess.png` | TESS dataset confusion matrix |
| `confusion_matrix_cremad.png` | CREMA-D dataset confusion matrix |

---

## 📊 Performance Benchmarks

### Expected Results:

| Metric | Expected Range | Notes |
|--------|----------------|-------|
| Overall Accuracy | 65-80% | Depends on dataset |
| Happy Recognition | 80-90% | Usually highest |
| Angry Recognition | 75-85% | High energy, distinct |
| Sad Recognition | 70-80% | Moderate |
| Fear Recognition | 60-75% | Often confused with sad |
| Neutral Recognition | 60-70% | Most challenging |
| Disgust Recognition | 65-75% | Moderate distinctiveness |

### Processing Speed:

| Operation | Time (approx) |
|-----------|---------------|
| Feature Extraction | 0.5-2 sec per file |
| Single Prediction | 0.1 sec |
| Training (10k files) | 20-30 minutes |
| Testing (100 files) | 1-2 minutes |

---

## 🐛 Troubleshooting

### Problem: Model not trained
```
⚠️ Model is not trained yet!
```
**Solution:**
```powershell
python train.py
```

### Problem: Audio file error
```
❌ Error: Audio file not found
```
**Solution:**
- Check file path
- Use quotes: `python predict.py "C:\path with spaces\file.wav"`
- Ensure file format is supported

### Problem: Import errors
```
ModuleNotFoundError: No module named 'librosa'
```
**Solution:**
```powershell
pip install -r requirements.txt
```

### Problem: PowerShell execution policy
```
.\run.ps1 : cannot be loaded because running scripts is disabled
```
**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 💡 Tips for Better Results

### 1. Audio Quality
- ✅ Use clear, high-quality recordings
- ✅ WAV format at 22050 Hz or higher
- ❌ Avoid heavily compressed MP3s
- ❌ Minimize background noise

### 2. Audio Duration
- ✅ 2-5 seconds is optimal
- ⚠️ Very short clips (< 1 sec) may be unreliable
- ⚠️ Very long clips (> 10 sec) may have mixed emotions

### 3. Recording Tips
- Speak clearly and expressively
- One emotion per clip
- Natural speech patterns
- Moderate speaking volume

---

## 🎯 Next Steps After Testing

1. ✅ Verify model works: `python predict.py sample.wav`
2. ✅ Check accuracy: `python test.py` → option 5
3. ✅ Test your audio: Record and predict
4. ✅ Fine-tune: Retrain with more data if needed
5. ✅ Deploy: Integrate into your application

---

## 📚 Additional Resources

- **QUICK_START.md** - Complete setup guide
- **README.md** - Project overview
- **train.py** - Training script source
- **predict.py** - Prediction script source
- **test.py** - Testing script source

---

## 🎤 Ready to Start?

Choose your path:

**Easiest:**
```powershell
.\run.ps1
```

**Quick test:**
```powershell
python predict.py sample.wav
```

**Full evaluation:**
```powershell
python test.py
```

**Happy Testing! 🚀**
