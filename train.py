import os
import numpy as np
import pickle
import lightgbm as lgb
import warnings
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from extract import extract_features
from tqdm import tqdm
from dataset_loader import DatasetLoader

# Filter warnings
warnings.filterwarnings('ignore', category=UserWarning)

# Dataset configuration
datasets = [
    {'path': 'TESS/', 'type': 'tess'},
    {'path': 'CREMA-D/', 'type': 'cremad'},  # Add CREMA-D dataset
]

# Load all datasets
X, y = [], []
total_files = 0

for dataset in datasets:
    loader = DatasetLoader.get_loader(dataset['type'])
    if not loader:
        print(f"Warning: No loader found for dataset type {dataset['type']}")
        continue
        
    print(f"\nLoading {dataset['type']} dataset from {dataset['path']}...")
    audio_files = loader(dataset['path'])
    total_files += len(audio_files)
    
    # Process files with progress bar
    pbar = tqdm(total=len(audio_files), desc=f"Processing {dataset['type']} files")
    
    for file_path, label in audio_files:
        try:
            features = extract_features(file_path)
            features = np.ravel(features)
            X.append(features)
            y.append(label)
        except Exception as e:
            print(f"\nError processing {file_path}: {e}")
        pbar.update(1)
    
    pbar.close()

# Convert to NumPy arrays
print("\nPreparing data...", end=" ", flush=True)
X = np.array(X)
y = np.array(y)
print("Done")

# Encode labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train LightGBM model
print("Training model...", end=" ", flush=True)
model = lgb.LGBMClassifier(verbose=-1)  # Disable verbose output
model.fit(X_train, y_train)
print("Done")

# Save model & label encoder
print("Saving model...", end=" ", flush=True)
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)
print("Done")

# Evaluate model
accuracy = model.score(X_test, y_test)
print(f"\nTest Accuracy: {accuracy:.2f}")
