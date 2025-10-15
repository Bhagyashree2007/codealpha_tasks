# Speech Emotion Recognition - Quick Start Guide

## 🚀 Complete Setup and Testing Guide

### Prerequisites
- Python 3.8 or higher
- Git with Git LFS installed
- At least 2GB free disk space

### Step 1: Install Dependencies

```powershell
# Create virtual environment (recommended)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install required packages
pip install -r requirements.txt

# If librosa installation fails, install audio backend first:
pip install soundfile
pip install librosa
```

### Step 2: Verify Dataset

```powershell
# Check if datasets are present
ls CREMA-D | Measure-Object
ls TESS | Measure-Object
```

**Expected output:**
- CREMA-D: 7,442 audio files
- TESS: 2,800 audio files

### Step 3: Train the Model

```powershell
python train.py
```

**What happens:**
- Loads TESS and CREMA-D datasets
- Extracts audio features (MFCCs, chroma, spectral contrast)
- Trains LightGBM classifier
- Saves `model.pkl` and `label_encoder.pkl`
- Shows test accuracy

**Expected time:** 15-30 minutes (depending on your CPU)

**Expected output:**
```
Loading tess dataset from TESS/...
Processing tess files: 100%|████████| 2800/2800
Loading cremad dataset from CREMA-D/...
Processing cremad files: 100%|████████| 7442/7442
Training model... Done
Test Accuracy: 0.XX
```

### Step 4: Test the Model

#### Option A: Quick Test on Sample File
```powershell
python predict.py sample.wav
```

**Expected output:**
```
Predicted Emotions with Confidence:

Happy: 76.61%
Angry: 6.42%
Disgust: 6.35%
Neutral: 6.04%
Sad: 2.41%
Fear: 2.17%
```

#### Option B: Interactive Test Suite
```powershell
python test.py
```

**Features:**
- Test on sample files
- Test on dataset samples
- View confusion matrices
- Get detailed classification reports
- Visual confidence bars

#### Option C: Test Your Own Audio
```powershell
python predict.py "path/to/your/audio.wav"
```

### Step 5: Evaluate Model Performance

```powershell
# Run comprehensive tests
python test.py
# Choose option 5 for quick evaluation on all datasets
```

**What you'll get:**
- Accuracy, Precision, Recall, F1-scores
- Confusion matrix visualization (saved as PNG)
- Per-emotion performance breakdown

---

## 📊 Understanding the Output

### Emotion Classes
The model predicts these 6 emotions:
- **Angry** - High energy, negative valence
- **Disgust** - Negative reaction
- **Fear** - Anxiety, worry
- **Happy** - Positive, joyful
- **Neutral** - Calm, no strong emotion
- **Sad** - Low energy, negative

### Confidence Scores
- **> 50%** - High confidence prediction
- **20-50%** - Moderate confidence
- **< 20%** - Low confidence (model uncertain)

---

## 🔧 Troubleshooting

### Issue: "Model not trained yet"
**Solution:**
```powershell
python train.py
```

### Issue: "Audio file not found"
**Solution:**
- Check file path is correct
- Use absolute paths or quotes: `python predict.py "C:\path\to\file.wav"`

### Issue: "Feature extraction failed"
**Solution:**
- Ensure audio format is supported (wav, mp3, flac, ogg)
- Check if audio file is corrupted
- Try converting to WAV format

### Issue: "Import errors"
**Solution:**
```powershell
pip install --upgrade -r requirements.txt
```

### Issue: Training takes too long
**Solution:**
- Reduce dataset size in `train.py` (modify the file loading)
- Use a smaller sample for initial testing

---

## 📁 Project Structure

```
Emotion recognition/
├── train.py              # Train the model
├── predict.py            # Predict emotion from audio
├── test.py               # Test suite with metrics
├── extract.py            # Feature extraction
├── dataset_loader.py     # Dataset loaders
├── requirements.txt      # Dependencies
├── sample.wav            # Sample audio file
├── model.pkl             # Trained model (after training)
├── label_encoder.pkl     # Label encoder (after training)
├── CREMA-D/              # CREMA-D dataset (7,442 files)
└── TESS/                 # TESS dataset (2,800 files)
```

---

## 🎯 Usage Examples

### Example 1: Basic Prediction
```powershell
python predict.py sample.wav
```

### Example 2: Batch Testing
```powershell
# Test multiple files
python predict.py CREMA-D/1001_DFA_ANG_XX.wav
python predict.py TESS/YAF_dog_happy.wav
```

### Example 3: Model Evaluation
```powershell
python test.py
# Select option 5 for comprehensive testing
```

---

## 📈 Expected Performance

Based on typical Speech Emotion Recognition models:

- **Overall Accuracy:** 65-80%
- **Best performing emotions:** Happy, Angry (high acoustic distinctiveness)
- **Challenging emotions:** Neutral, Fear (subtle acoustic differences)

---

## 🔄 Retraining the Model

If you want to retrain with different parameters:

```powershell
# Delete old model files
rm model.pkl, label_encoder.pkl

# Retrain
python train.py
```

---

## 🚀 Next Steps

1. **✅ Verify installation:** `pip list`
2. **✅ Train model:** `python train.py`
3. **✅ Test on sample:** `python predict.py sample.wav`
4. **✅ Run test suite:** `python test.py`
5. **✅ Try your own audio files**

---

## 💡 Tips for Better Results

1. **Audio Quality:** Use clear, well-recorded audio
2. **Format:** WAV format works best
3. **Duration:** 2-5 second clips are optimal
4. **Background noise:** Minimize for better accuracy

---

## 📞 Quick Commands Reference

```powershell
# Setup
pip install -r requirements.txt

# Train
python train.py

# Predict
python predict.py <audio-file>

# Test
python test.py

# Check git status
git status

# Count dataset files
(Get-ChildItem -Recurse CREMA-D -File).Count
(Get-ChildItem -Recurse TESS -File).Count
```

---

**🎤 Happy Emotion Recognition!**
