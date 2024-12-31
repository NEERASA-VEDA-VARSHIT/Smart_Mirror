import pyttsx3
import logging

class TextToSpeech:
    """
    Class for converting text to speech.
    """
    def __init__(self, config):
        """
        Initialize the speech engine with configuration settings.
        """
        self.engine = pyttsx3.init()

        self.engine.setProperty('rate', config['rate'])
        self.engine.setProperty('volume', config['volume'])

    def speak(self, text):
        """
        Speak the given text.
        
        :param text: The text to be spoken.
        """
        try:
            logging.info(f"Speaking: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            logging.error(f"Error generating audio: {e}")
