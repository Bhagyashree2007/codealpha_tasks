import os
from typing import List, Tuple, Dict

class DatasetLoader:
    # Standardized emotion mapping
    EMOTION_MAP = {
        # TESS mappings
        'angry': 'ang',
        'disgust': 'dis',
        'fear': 'fea',
        'happy': 'hap',
        'neutral': 'neu',
        'pleasant surprise': 'sur',
        'sad': 'sad',
        # CREMA-D mappings
        'ang': 'ang',
        'dis': 'dis',
        'fea': 'fea',
        'hap': 'hap',
        'neu': 'neu',
        'sad': 'sad'
    }

    @staticmethod
    def load_tess(dataset_path: str) -> List[Tuple[str, str]]:
        """Load TESS dataset - handles both OAF and YAF patterns"""
        audio_files = []
        for folder in os.listdir(dataset_path):
            folder_path = os.path.join(dataset_path, folder)
            
            if not os.path.isdir(folder_path) or folder.startswith('.'):
                continue
            
            for file in os.listdir(folder_path):
                if any(file.lower().endswith(ext) for ext in {".wav", ".mp3", ".m4a", ".flac", ".ogg"}):
                    # Handle both OAF_word_emotion.wav and YAF_word_emotion.wav
                    if file.startswith(('OAF_', 'YAF_')):
                        parts = file.split('_')
                        if len(parts) >= 3:
                            emotion = parts[-1].replace('.wav', '').lower()
                            emotion = DatasetLoader.EMOTION_MAP.get(emotion, emotion)
                            audio_files.append((os.path.join(folder_path, file), emotion))
        
        return audio_files

    @staticmethod
    def load_custom(dataset_path: str) -> List[Tuple[str, str]]:
        """Template for loading custom dataset - implement based on structure"""
        audio_files = []
        # Implement custom dataset loading logic here
        return audio_files

    @staticmethod
    def load_cremad(path):
        audio_files = []
        for filename in os.listdir(path):
            if filename.endswith('.wav'):
                # CREMA-D filename format: 1076_MTI_SAD_XX_LOW.wav
                # where SAD is the emotion label and LOW is the intensity
                parts = filename.split('_')
                if len(parts) >= 4:
                    emotion = parts[2].lower()
                    emotion = DatasetLoader.EMOTION_MAP.get(emotion, emotion)
                    # Extract confidence score if available (might be in metadata)
                    try:
                        confidence_file = filename.replace('.wav', '_confidence.txt')
                        confidence_path = os.path.join(path, confidence_file)
                        if os.path.exists(confidence_path):
                            with open(confidence_path, 'r') as f:
                                confidence = float(f.read().strip())
                            if confidence > 0:  # Only include samples with confidence > 0
                                audio_files.append((os.path.join(path, filename), emotion))
                        else:
                            # If no confidence file exists, include the sample
                            audio_files.append((os.path.join(path, filename), emotion))
                    except:
                        # If there's any error reading confidence, include the sample
                        audio_files.append((os.path.join(path, filename), emotion))
        return audio_files

    @staticmethod
    def get_loader(dataset_type: str):
        """Get appropriate loader function for dataset type"""
        loaders = {
            'tess': DatasetLoader.load_tess,
            'custom': DatasetLoader.load_custom,
            'cremad': DatasetLoader.load_cremad  # Add CREMA-D loader
        }
        return loaders.get(dataset_type)
