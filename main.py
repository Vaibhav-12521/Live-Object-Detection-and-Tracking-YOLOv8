import cv2
import numpy as np
from ultralytics import YOLO
from collections import defaultdict


class ObjectdetectTracker:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)
        self.track_history = defaultdict(lambda: [])
        
    def detect_live(self, camera_id=0):
        cap = cv2.VideoCapture(camera_id)
        if not cap.isOpened():
            return
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            results = self.model.track(frame, persist=True, verbose=False)
            if results[0].boxes.id is not None:
                annotated_frame = results[0].plot()
            else:
                annotated_frame = results[0].plot()
            fps = cap.get(cv2.CAP_PROP_FPS)
            cv2.putText(annotated_frame, f'FPS: {int(fps)}', (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Live Object Detection & Tracking', annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    def get_class_names(self):
        return self.model.names


def main():
    detect = ObjectdetectTracker(model_path='yolov8n.pt')
    detect.detect_live(camera_id=0)
    

if __name__ == "__main__":
    main()
