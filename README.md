Here’s the complete **`README.md`** file content for your GitHub repository:

---

````markdown
# 🎯 Live Object Detection and Tracking using YOLOv8 and OpenCV

This project demonstrates **real-time object detection and tracking** using the **Ultralytics YOLOv8** model integrated with **OpenCV**.  
It captures your webcam feed to identify and track objects with unique IDs and displays FPS on the live video.

---

## 🚀 Features

- 🧠 Real-time **object detection and tracking**
- 🎥 Live **webcam feed** integration
- ⚡ Displays **FPS (Frames Per Second)** for performance
- 🧭 Unique **object ID tracking**
- 🧱 Simple and modular **class-based structure**

---

## 🧰 Technologies Used

- **Python 3.8+**
- **OpenCV**
- **NumPy**
- **Ultralytics YOLOv8**

---

## 📦 Installation

Clone this repository:
```bash
git clone https://github.com/Vaibhav-12521/Live-Object-Detection-and-Tracking-YOLOv8.git
cd Live-Object-Detection-and-Tracking-YOLOv8
````

Install dependencies:

```bash
pip install opencv-python ultralytics numpy
```

---

## ▶️ Usage

Run the live object detection:

```bash
python main.py
```

Press **'q'** to quit the window.

---

## 📂 Project Structure

```
📦 Live-Object-Detection-and-Tracking-YOLOv8
├── main.py                  # Main script for live detection and tracking
├── yolov8n.pt               # YOLOv8 model file (downloaded automatically if missing)
├── README.md                # Project documentation
└── requirements.txt         # Required dependencies
```

---

## 💻 Code Overview

```python
from ultralytics import YOLO
import cv2
import numpy as np
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
            annotated_frame = results[0].plot()
            fps = cap.get(cv2.CAP_PROP_FPS)
            cv2.putText(annotated_frame, f'FPS: {int(fps)}', (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Live Object Detection & Tracking', annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
```

---

## 📸 Output Preview

|  🎬 | Description                           |
| :-: | :------------------------------------ |
|  🧍 | Detects multiple objects in real-time |
|  🧭 | Tracks them with unique IDs           |
|  ⚙️ | Displays FPS and bounding boxes       |

---

## 🏆 Future Enhancements

* 🚗 Vehicle counting and motion tracking
* 🧍 Human pose detection
* 📊 Object analytics dashboard
* 💾 Option to save detection results as video

---

## 👨‍💻 Author

**Vaibhav Singh**
🔗 [GitHub Profile](https://github.com/Vaibhav-12521)
💬 *If you like this project, give it a ⭐ on GitHub!*

---


Would you like me to add a **project banner (image + shields badges)** section at the top for a more professional GitHub look?
```
