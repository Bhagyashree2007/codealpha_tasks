import numpy as np
import pickle
import warnings
import os
import sys
from collections import defaultdict
from extract import extract_features

# Suppress unnecessary warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

# Check if model and label encoder exist before loading
MODEL_FILE = "model.pkl"
LABEL_ENCODER_FILE = "label_encoder.pkl"

if not os.path.exists(MODEL_FILE) or not os.path.exists(LABEL_ENCODER_FILE):
    print("\n⚠️ Model is not trained yet! Please train the model first (missing model.pkl or label_encoder.pkl).")
    exit()

# Load trained model and label encoder
with open(MODEL_FILE, "rb") as f:
    model = pickle.load(f)
with open(LABEL_ENCODER_FILE, "rb") as f:
    label_encoder = pickle.load(f)

print("✅ Model loaded successfully!\n")

# Updated the emotion mapping dictionary
EMOTION_FULL_NAMES = {
    'ang': 'Angry',
    'dis': 'Disgust',
    'fea': 'Fear',
    'hap': 'Happy',
    'neu': 'Neutral',
    'sad': 'Sad',
    'sur': 'Surprise',
    'ps': 'Surprise',
    'angry': 'Angry',
    'disgust': 'Disgust',
    'fear': 'Fear',
    'happy': 'Happy',
    'neutral': 'Neutral',
    'sad': 'Sad',
    'surprise': 'Surprise',
    'pleasant_surprise': 'Surprise',
    'pleasant_surprised': 'Surprise',
    'pleasant surprise': 'Surprise'
}

def predict_emotion(file_path):
    try:
        # Extract features
        features = extract_features(file_path)
        if features is None:
            return None  # Handle cases where feature extraction fails

        # Predict probabilities for each emotion
        probabilities = model.predict_proba(features)[0]
        sorted_indices = np.argsort(probabilities)[::-1]  # Sort in descending order

        emotion_confidence = defaultdict(float)

        for i in sorted_indices:
            confidence = probabilities[i] * 100
            if confidence > 0.0:  # Ignore zero-confidence predictions
                emotion = label_encoder.inverse_transform([i])[0]
                # Standardize the emotion name
                emotion = emotion.replace("OAF_", "").replace("YAF_", "")
                emotion = emotion.lower()
                emotion = emotion.replace(" ", "_")  # Handle spaces consistently
                
                # Map to standardized emotion name and skip if not in our mapping
                emotion = EMOTION_FULL_NAMES.get(emotion)
                if emotion:  # Only add to results if we have a valid mapping
                    emotion_confidence[emotion] += confidence

        # Sort final results by confidence
        sorted_results = sorted(emotion_confidence.items(), key=lambda x: x[1], reverse=True)
        
        return sorted_results if sorted_results else None

    except Exception as e:
        print(f"⚠️ Error processing file: {e}")
        return None  # Return None if there's an error

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("🎯 Speech Emotion Recognition")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Usage:")
        print("  python predict.py <path-to-audio-file>")
        print("\nExample:")
        print("  python predict.py sample.wav")
        print("\nSupported formats: wav, mp3, ogg, flac")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
        sys.exit(1)

    audio_file = sys.argv[1]
    if not os.path.exists(audio_file):
        print(f"\n❌ Error: Audio file not found: {audio_file}")
        print("Please check the file path and try again.\n")
        sys.exit(1)

    results = predict_emotion(audio_file)

    # Print results in a clean format
    if results:
        print("Predicted Emotions with Confidence:\n")
        # Filter out zero confidence predictions and sort
        sorted_predictions = [(emotion, conf) for emotion, conf in results if conf > 0.001]
        
        # Display only non-zero predictions
        for emotion, confidence in sorted_predictions:
            print(f"{emotion}: {confidence:.2f}%")
    else:
        print("\n⚠️ Could not process the audio file. Please check the format and try again.")
