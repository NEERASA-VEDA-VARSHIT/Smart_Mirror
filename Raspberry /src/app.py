import random
import logging
import yaml
import cv2
from emotion_detector import EmotionDetector
from text_to_speech import TextToSpeech
from gui import EmotionDetectionGUI

class EmotionDetectionApp:
    """
    The main application class for real-time emotion detection.
    """
    def __init__(self, config_file="config/config.yaml"):
        """
        Initialize the application with configuration settings.
        """
        self.config = self._load_config(config_file)
        self.emotion_detector = EmotionDetector(self.config['emotion_detector'])
        self.text_to_speech = TextToSpeech(self.config['text_to_speech'])
        self.gui = EmotionDetectionGUI()  # GUI (optional, could be omitted for Pi)

        self.compliments = self.config['compliments']

    def _load_config(self, config_file):
        """
        Load the configuration from a YAML file.
        
        :param config_file: Path to the YAML configuration file.
        :return: Loaded configuration as a dictionary.
        """
        try:
            with open(config_file, 'r') as f:
                config = yaml.safe_load(f)
            return config
        except Exception as e:
            logging.error(f"Error loading config file: {e}")
            raise e

    def process_frame(self, frame):
        """
        Process a frame from the webcam, detect emotion, and provide feedback.
        
        :param frame: The frame captured from the webcam.
        """
        try:
            emotion = self.emotion_detector.detect_emotion(frame)
            compliment = random.choice(self.compliments.get(emotion, ["You're amazing just the way you are!"]))

            self.gui.update_labels(emotion, compliment)  # Update GUI (optional)
            self.text_to_speech.speak(compliment)

        except Exception as e:
            logging.error(f"Error processing frame: {e}")

    def start(self, webcam_capture_func):
        """
        Start the application, capturing frames from the webcam.
        
        :param webcam_capture_func: Function to capture and process webcam frames.
        """
        webcam_capture_func(self.process_frame)
        self.gui.start()  # Start GUI if needed
