# 🤟 Hand Sign Language Detection with Real-Time Webcam Input

A real-time hand sign language recognition system using computer vision and deep learning. Built with OpenCV, cvzone, and a custom-trained Keras model, this tool detects and classifies ASL (A–Z) hand gestures using your webcam.

---

## 📌 Features

- 📷 Real-time webcam hand tracking
- ✋ Detects hand gestures A–Z
- 🧠 Integrates a trained Keras classification model
- 🖼️ Live GUI preview using Tkinter
- 🔄 Continuous detection with smooth frame updates

---

## 🛠️ Tech Stack

- Python 3
- OpenCV (`cv2`)
- cvzone (HandTrackingModule, ClassificationModule)
- TensorFlow/Keras (`.h5` model)
- NumPy, Math
- Tkinter for GUI
- PIL (Pillow) for image display

---

## 🚀 How to Run

1. **Install dependencies**:
   ```bash
   pip install opencv-python cvzone numpy Pillow
   
 2.	Make sure you have the following files:
	•	final_code.py – main script
	•	Model/keras_model.h5 – trained model
	•	Model/labels.txt – corresponding labels file
3.	Run the application:
   python final_code.py
