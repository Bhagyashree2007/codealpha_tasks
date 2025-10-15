import librosa
import numpy as np
import soundfile as sf

def extract_features(file_path, target_length=22050 * 3):  # 3 sec audio
    try:
        # Try loading with SoundFile first (better quality)
        with sf.SoundFile(file_path) as audio:
            y = audio.read(dtype="float32")
            sr = audio.samplerate
    except:
        # Fallback to librosa (handles more formats)
        y, sr = librosa.load(file_path, sr=22050)

    # Convert stereo to mono if needed
    if len(y.shape) > 1:
        y = np.mean(y, axis=1)

    # Trim silent parts
    y, _ = librosa.effects.trim(y)

    # Ensure fixed length (pad or trim)
    if len(y) < target_length:
        y = np.pad(y, (0, target_length - len(y)), mode="constant")
    else:
        y = y[:target_length]

    # Extract MFCC features
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40, n_fft=512)
    return np.mean(mfcc, axis=1).reshape(1, -1)  # Reshape to avoid sklearn warning
