# AutoVision – Real-Time Object Detection with Speech Feedback

## Overview
AutoVision is an embedded computer vision assistive system designed to help visually impaired individuals perceive their surroundings through audio feedback. The system runs on a **Raspberry Pi with a Pi Camera**, performing real-time object detection using **SSD MobileNet V3** trained on the **COCO dataset**, and converting detected object labels into speech using **Google Text-to-Speech (gTTS)**.

The system captures live video frames, detects objects using a deep neural network, extracts semantic labels, and generates real-time audio feedback describing the detected objects.

This project demonstrates **edge AI deployment under embedded hardware constraints**, integrating sensing, perception, and speech synthesis into a single pipeline.

---

# System Architecture

Pipeline:

Camera Input → Frame Preprocessing → SSD MobileNet Detection → Non-Maximum Suppression → Object Label Extraction → gTTS Speech Output

Components:

- Raspberry Pi 3B+  
- Raspberry Pi Camera Module (1080p)  
- OpenCV DNN module  
- SSD MobileNet V3 object detection model  
- COCO dataset labels  
- Google Text-to-Speech (gTTS)

---

# Features

- Real-time object detection using **SSD MobileNet V3**
- Pretrained **COCO dataset with 80 object classes**
- Embedded deployment on **Raspberry Pi without GPU**
- Dynamic **speech feedback for detected objects**
- Multi-object detection with bounding boxes
- Lightweight edge AI implementation

---

# Object Classes

The detection model is trained on the **COCO dataset**, which contains **80 common object categories**.

Examples include:

- Person  
- Car  
- Bicycle  
- Chair  
- Laptop  
- Bottle  
- Cell phone  
- Book  
- Dog  
- Cat  
- Bus  
- Truck  

These class labels are loaded from the file: coco.names



Each detected object is mapped to its corresponding class name and passed to the speech module.

---

# Hardware Requirements

- Raspberry Pi 3B+ (or newer recommended)
- Raspberry Pi Camera Module
- MicroSD card with Raspberry Pi OS
- Power supply / power bank
- Headphones or speaker (audio output)

---

# Software Prerequisites

- Python 3.7+
- OpenCV
- NumPy
- gTTS
- playsound

---

# Installation Guide

## 1 Install Raspberry Pi OS

Flash Raspberry Pi OS onto the SD card using Raspberry Pi Imager.

Enable the camera interface: sudo raspi-config



Navigate to: Interface Options → Camera → Enable


Reboot the system.

---

## 2 Update System

```bash
sudo apt update
sudo apt upgrade
```
---

## 3 Install Python Dependencies

```bash
pip install opencv-python
pip install numpy
pip install gTTS
pip install playsound
```


Optional for better OpenCV support:
```bash
pip install opencv-contrib-python
```

---

## 4 Download Model Files

Download the following files and place them in the project directory.

Model weights:

frozen_inference_graph.pb


Model configuration:  ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt


Class labels:

coco.names


---

# Project Structure

```bash
Audio-Vision-ML_Project/
│
├── main.py
├── obj_speach.py
├── coco.names
├── frozen_inference_graph.pb
├── ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt
├── new.mp3
└── README.md
```
---

# Workflow Explanation

## 1 Camera Capture

The Raspberry Pi camera continuously captures frames using **OpenCV**.

```python
import cv2

cap = cv2.VideoCapture(0)

```


## 2 Object Detection

The system loads the SSD MobileNet V3 detection network using OpenCV's DNN module.


```python
net = cv2.dnn_DetectionModel(weightsPath, configPath)
```
The input frame is processed and objects are detected using:

Confidence threshold
Non-Maximum Suppression (NMS)
```python
classIds, confs, bbox = net.detect(img, confThreshold=0.45, nmsThreshold=0.2)
```
Bounding boxes and labels are drawn on detected objects.

## 3 Label Extraction

Detected objects are mapped to their class names using the COCO label list.

Example detected labels:
person
chair
bottle

## 4 Speech Generation

Detected object names are converted to speech using Google Text-to-Speech (gTTS).

```python
output = gTTS(text=final, lang='en', slow=False)
output.save("new.mp3")
```

Running the Project

## Start the object detection system:
python main.py





