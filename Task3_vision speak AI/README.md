# VisionSpeak AI

## Project Overview

VisionSpeak AI is an AI-powered Image Captioning application developed using Python. The application allows users to upload an image and automatically generate meaningful captions using the Salesforce BLIP (Bootstrapping Language-Image Pre-training) model. It also includes Text-to-Speech functionality, enabling the generated caption to be spoken aloud for better accessibility and user interaction.

## Features

* Upload and analyze images
* Generate AI-powered image captions
* Normal and Detailed caption modes
* Text-to-Speech output using pyttsx3
* Save generated captions to a text file
* Simple and user-friendly GUI built with Tkinter

## Technologies Used

* Python
* Tkinter
* Hugging Face Transformers
* Salesforce BLIP Model
* PyTorch
* Pillow (PIL)
* pyttsx3

## Installation

1. Clone the repository:

```bash
git clone https://github.com/shraddhachauhan-hub/CODSOFT.git
```

2. Navigate to the project folder:

```bash
cd "Task3_vision speak AI"
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```



## How to Run

Run the following command:

```bash
python vision_speak_gui.py
```

The application window will open, allowing you to upload an image and generate captions.



## How It Works

1. Upload an image through the GUI.
2. The BLIP model analyzes the image.
3. A caption is generated automatically.
4. Users can choose Normal or Detailed caption mode.
5. The generated caption can be spoken aloud using Text-to-Speech.
6. Captions can be saved for future reference.



## Project Structure

```text
Task3_vision speak AI/
│
├── assets/
├── app.py
├── vision_speak_gui.py
├── requirements.txt
├── captions.txt
├── test.jpg
├── README.md
└── Video Project 5.mp4
```



## Future Enhancements

* Multi-language caption generation
* OCR-based text extraction from images
* Real-time webcam captioning
* Video caption generation
* Cloud deployment



## Author

**Shraddha Chauhan**

CodSoft AI Internship – Task 3

VisionSpeak AI – AI-Powered Image Captioning Application
