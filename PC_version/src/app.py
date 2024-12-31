import random
import logging
from emotion_detector import EmotionDetector
from text_to_speech import TextToSpeech
from gui import EmotionDetectionGUI

class EmotionDetectionApp:
    """
    The main application class which orchestrates the emotion detection, text-to-speech, and GUI.
    """
    def __init__(self):
        """
        Initialize the application components.
        """
        self.emotion_detector = EmotionDetector()  # Handles emotion detection
        self.text_to_speech = TextToSpeech()  # Handles text-to-speech
        self.gui = EmotionDetectionGUI()  # Handles the GUI

        self.compliments = self._initialize_compliments()

    def _initialize_compliments(self):
        """
        Initialize the compliments for different emotions.
        """
        return {
            'happy': [
                "Your smile lights up the room!",
                "You bring so much joy to everyone around you!",
                "Keep shining, you're amazing!",
                "Your happiness is contagious, keep spreading it!"
            ],
            'neutral': [
                "Your presence is calm and confident.",
                "You handle things so gracefully.",
                "You have a great sense of balance.",
                "You give off such a peaceful vibe!"
            ],
            'sad': [
                "You've got this, keep going! It’s okay to feel down, but better days are ahead.",
                "It's tough right now, but you're stronger than you think.",
                "Every step forward is progress, even if it's small.",
                "I'm rooting for you, hang in there!"
            ],
            'angry': [
                "Take a deep breath, everything will be alright.",
                "Anger is just a moment, your peace is forever.",
                "It's okay to feel angry, but don't let it control you.",
                "You have the power to let go of the anger."
            ],
            'surprise': [
                "You look wonderfully surprised today!",
                "What an unexpected delight, you seem full of wonder!",
                "Surprise suits you well!",
                "You never fail to amaze with your reactions!"
            ],
            'fear': [
                "Stay strong, you're doing great!",
                "Fear is natural, but you can overcome it.",
                "Courage doesn't mean you're not afraid, it means you move forward anyway.",
                "Take a deep breath, you're braver than you think."
            ]
        }

    def process_frame(self, frame):
        """
        Process each frame from the webcam, detect emotion, and provide feedback.

        :param frame: The frame captured from the webcam.
        """
        try:
            emotion = self.emotion_detector.detect_emotion(frame)
            compliment = random.choice(self.compliments.get(emotion, ["You're amazing just the way you are!"]))

            self.gui.update_labels(emotion, compliment)
            self.text_to_speech.speak(compliment)

        except Exception as e:
            logging.error(f"Error processing frame: {e}")

    def start(self, webcam_capture_func):
        """
        Start the emotion detection process with webcam capture.

        :param webcam_capture_func: The function to capture webcam frames.
        """
        webcam_capture_func(self.process_frame)
        self.gui.start()

