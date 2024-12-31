import cv2
from app import EmotionDetectionApp

def capture_webcam(process_frame_func):
    """
    Capture frames from the webcam and process them.
    
    :param process_frame_func: Function to process each captured frame.
    """
    cap = cv2.VideoCapture(0)  # Adjust for Pi Camera if needed
    if not cap.isOpened():
        raise Exception("Could not open webcam.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            raise Exception("Failed to grab frame.")
        
        process_frame_func(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    app = EmotionDetectionApp()
    app.start(capture_webcam)
