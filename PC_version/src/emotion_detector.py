from fer import FER

class EmotionDetector:
    """
    Class responsible for detecting emotions from a given image frame.
    """
    def __init__(self):
        """
        Initialize the emotion detector using MTCNN for better face detection.
        """
        self.emotion_detector = FER(mtcnn=True)

    def detect_emotion(self, frame):
        """
        Detect the dominant emotion from the given image frame.

        :param frame: The frame captured from the webcam.
        :return: The detected emotion.
        """
        emotion, _ = self.emotion_detector.top_emotion(frame)
        return emotion

