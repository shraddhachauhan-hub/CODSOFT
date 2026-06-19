# FaceGuard AI

An AI-powered Face Detection and Recognition System built using Python and OpenCV.

## Overview

FaceGuard AI is a real-time face recognition application that detects faces through a webcam, recognizes registered users, and automatically records attendance with date and time.

This project demonstrates Computer Vision, Face Detection, Face Recognition, Dataset Creation, Model Training, and Attendance Automation.


## Features

- Real-Time Face Detection
- Face Recognition using LBPH Algorithm
- Automatic Attendance Logging
- Confidence Score Display
- Unknown Face Detection
- Face Counter
- Duplicate Attendance Prevention
- Easy Dataset Registration
- Model Training Module

## Technologies Used

- Python
- OpenCV
- NumPy
- Pandas
- Pillow


## Project Structure

Task5_FaceGuard_AI/

├── assets/

├── attendance/

│ └── attendance.csv

├── dataset/

│ └── user_images

├── models/

│ └── trainer.yml

├── app.py

├── face_trainer.py

├── train_model.py

├── requirements.txt

└── README.md

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Task5_FaceGuard_AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Step 1: Register Face

```bash
python face_trainer.py
```

Enter your name and collect face samples.

### Step 2: Train Model

```bash
python train_model.py
```

This generates:

```text
models/trainer.yml
```

### Step 3: Start Recognition System

```bash
python app.py
```

Press ESC to exit.

## Attendance Output

Example:

| Name | Date | Time |
|------|------|------|
| shraddha | 2026-06-18 | 12:05:30 |


## Future Enhancements

- GUI Dashboard
- Multi-Person Recognition
- Face Recognition from Images
- Attendance Analytics
- Cloud Database Integration

## Author

Shraddha Chauhan

B.Tech Information Technology

CodSoft Artificial Intelligence Internship