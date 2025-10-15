
"""
Test script for Speech Emotion Recognition model
Tests the model on multiple sample files and provides evaluation metrics
"""
import os
import numpy as np
import pickle
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from extract import extract_features
from dataset_loader import DatasetLoader
from tqdm import tqdm
import warnings

warnings.filterwarnings('ignore')

def load_model():
    """Load the trained model and label encoder"""
    if not os.path.exists("model.pkl") or not os.path.exists("label_encoder.pkl"):
        print("\n❌ Error: Model files not found!")
        print("Please run 'python train.py' first to train the model.\n")
        return None, None
    
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("label_encoder.pkl", "rb") as f:
        label_encoder = pickle.load(f)
    
    return model, label_encoder

def test_on_dataset(dataset_path, dataset_type, model, label_encoder, max_samples=100):
    """Test the model on a specific dataset"""
    print(f"\n{'='*60}")
    print(f"Testing on {dataset_type.upper()} dataset")
    print(f"{'='*60}")
    
    loader = DatasetLoader.get_loader(dataset_type)
    if not loader:
        print(f"❌ No loader found for {dataset_type}")
        return
    
    audio_files = loader(dataset_path)
    
    # Limit samples for faster testing
    if len(audio_files) > max_samples:
        print(f"📊 Testing on {max_samples} random samples (out of {len(audio_files)} total)")
        np.random.shuffle(audio_files)
        audio_files = audio_files[:max_samples]
    else:
        print(f"📊 Testing on all {len(audio_files)} files")
    
    y_true = []
    y_pred = []
    
    pbar = tqdm(audio_files, desc="Testing")
    for file_path, true_label in pbar:
        try:
            features = extract_features(file_path)
            features = np.ravel(features).reshape(1, -1)
            
            prediction = model.predict(features)[0]
            predicted_label = label_encoder.inverse_transform([prediction])[0]
            
            y_true.append(true_label)
            y_pred.append(predicted_label)
        except Exception as e:
            print(f"\n⚠️  Error processing {file_path}: {e}")
    
    pbar.close()
    
    # Calculate metrics
    if y_true:
        print("\n📈 Classification Report:")
        print(classification_report(y_true, y_pred))
        
        # Confusion matrix
        cm = confusion_matrix(y_true, y_pred, labels=label_encoder.classes_)
        plot_confusion_matrix(cm, label_encoder.classes_, dataset_type)
        
        accuracy = np.mean(np.array(y_true) == np.array(y_pred))
        print(f"\n✅ Overall Accuracy: {accuracy:.2%}\n")
    else:
        print("\n❌ No valid predictions made!")

def plot_confusion_matrix(cm, labels, dataset_name):
    """Plot confusion matrix"""
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=labels, yticklabels=labels)
    plt.title(f'Confusion Matrix - {dataset_name.upper()}')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.tight_layout()
    
    output_file = f'confusion_matrix_{dataset_name}.png'
    plt.savefig(output_file)
    print(f"\n📊 Confusion matrix saved as '{output_file}'")
    plt.close()

def test_single_file(file_path, model, label_encoder):
    """Test on a single audio file"""
    print(f"\n{'='*60}")
    print(f"Testing single file: {file_path}")
    print(f"{'='*60}")
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return
    
    try:
        features = extract_features(file_path)
        features = np.ravel(features).reshape(1, -1)
        
        # Get prediction probabilities
        probabilities = model.predict_proba(features)[0]
        sorted_indices = np.argsort(probabilities)[::-1]
        
        print("\n🎯 Prediction Results:")
        print("-" * 40)
        for i in sorted_indices:
            emotion = label_encoder.inverse_transform([i])[0]
            confidence = probabilities[i] * 100
            if confidence > 0.01:  # Only show meaningful predictions
                bar = "█" * int(confidence / 2)
                print(f"{emotion:15s} {confidence:6.2f}% {bar}")
        print("-" * 40)
        
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Main test function"""
    print("\n" + "="*60)
    print("🎤 SPEECH EMOTION RECOGNITION - TEST SUITE")
    print("="*60)
    
    # Load model
    model, label_encoder = load_model()
    if model is None:
        return
    
    print("✅ Model loaded successfully!")
    print(f"📋 Emotion classes: {', '.join(label_encoder.classes_)}")
    
    # Menu
    print("\n" + "="*60)
    print("Select test option:")
    print("="*60)
    print("1. Test on sample.wav")
    print("2. Test on TESS dataset (sample)")
    print("3. Test on CREMA-D dataset (sample)")
    print("4. Test on custom audio file")
    print("5. Quick test on all datasets")
    print("="*60)
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice == '1':
        test_single_file('sample.wav', model, label_encoder)
    
    elif choice == '2':
        if os.path.exists('TESS/'):
            test_on_dataset('TESS/', 'tess', model, label_encoder, max_samples=50)
        else:
            print("❌ TESS dataset not found!")
    
    elif choice == '3':
        if os.path.exists('CREMA-D/'):
            test_on_dataset('CREMA-D/', 'cremad', model, label_encoder, max_samples=50)
        else:
            print("❌ CREMA-D dataset not found!")
    
    elif choice == '4':
        file_path = input("Enter audio file path: ").strip()
        test_single_file(file_path, model, label_encoder)
    
    elif choice == '5':
        datasets = [
            ('TESS/', 'tess'),
            ('CREMA-D/', 'cremad')
        ]
        for path, dtype in datasets:
            if os.path.exists(path):
                test_on_dataset(path, dtype, model, label_encoder, max_samples=30)
    
    else:
        print("❌ Invalid choice!")
    
    print("\n" + "="*60)
    print("✅ Testing complete!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
