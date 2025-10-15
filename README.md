# **Emotion Recognition from Speech(SER)**  

Speech carries not just words but also emotional cues. By analyzing the acoustic properties of speech, this project detects and classifies emotions using Mel-Frequency Cepstral Coefficients (MFCCs) and neural network models such as CNN, RNN, and LSTM.The project demonstrates a complete machine learning pipeline — from raw audio preprocessing and feature extraction to model training, evaluation, and deployment.
This project utilizes machine learning to analyze speech and classify emotions with confidence scores. It extracts features from audio files and uses a trained model to predict emotions.  

## **How It Works**  
- Extracts key features from audio using `librosa`.
- Uses a trained **LightGBM classifier** to predict emotions.
- Displays the predicted emotions with confidence scores.

## **Key Features**
🎧 Speech Preprocessing – resampling, trimming, normalization, and silence removal

🔊 Feature Extraction – MFCCs, delta coefficients, chroma, spectral contrast, and mel-spectrograms

🧩 Deep Learning Models – CNN, RNN, Bi-LSTM, and hybrid CNN+LSTM architectures

🧪 Datasets – Compatible with RAVDESS, TESS, and EMO-DB datasets

📈 Evaluation Metrics – Accuracy, Precision, Recall, F1-score, and Confusion Matrix visualization

🚀 Future Scope – Real-time emotion detection via microphone input and mobile deployment using TensorFlow Lite

## **How to Use**  

### **1. Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **2. Train the Model**  
```sh
python train.py
```
- Processes the datasets and saves `model.pkl` and `label_encoder.pkl`.  

### **3. Predict Emotions from an Audio File**  
```sh
python predict.py <path-to-audio-file>
```

**Example:**  
```sh
python predict.py sample.wav
```

### **Output Example:**  
```
Predicted Emotions with Confidence:

Happy: 76.61%
Angry: 6.42%
Disgust: 6.35%
Neutral: 6.04%
Sad: 2.41%
Fear: 2.17%
```

## **Points to Remember**  
- Run `python train.py` first.  
- Ensure the correct file path is used.  
- Use `.wav`, `.mp3`, `.ogg`, or `.flac` audio formats.  

This project enables robust speech emotion recognition using machine learning techniques.

