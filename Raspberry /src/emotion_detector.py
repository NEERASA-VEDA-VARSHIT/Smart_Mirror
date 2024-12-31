import cv2
from fer import FER

class EmotionDetector:
    """
    Class for detecting emotions from faces in images.
    """
    def __init__(self, config):
        """
        Initialize the Emotion Detector with the required configurations.
        """
        self.detector = FER(mtcnn=True)  # Using MTCNN for better face detection

    def detect_emotion(self, frame):
        """
        Detect the emotion of the face in the given frame.
        
        :param frame: The frame captured from the webcam.
        :return: The detected emotion.
        """
        try:
            emotion, _ = self.detector.top_emotion(frame)
            return emotion
        except Exception as e:
            logging.error(f"Error detecting emotion: {e}")
            return "neutral"
