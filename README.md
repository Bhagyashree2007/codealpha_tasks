# **Speech Emotion Recognition (SER)**  

This project utilizes machine learning to analyze speech and classify emotions with confidence scores. It extracts features from audio files and uses a trained model to predict emotions.  

## **How It Works**  
- Extracts key features from audio using `librosa`.
- Uses a trained **LightGBM classifier** to predict emotions.
- Displays the predicted emotions with confidence scores.

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

## **Note**  
- Run `python train.py` first.  
- Ensure the correct file path is used.  
- Use `.wav`, `.mp3`, `.ogg`, or `.flac` audio formats.  

This project enables robust speech emotion recognition using machine learning techniques.

