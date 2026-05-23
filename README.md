# Basic Hand-Tracker using Python.
A very small and basic python program to control a drone or aerial device using hand gestures shown to the program via CV2.

# Developers note:
This is my first ever github post. This project is first of many to come and hopefully not the last.

# Requirements:
This project requires:
  - **OpenCV** ('opencv-python'), which handles the video footage and image processing.
  - **Google's MediaPipe** ('mediapipe'), which does most of the heavy lifting by using Google's Open Source high fidelity hand tracking and finger detection module. Required version is **0.10.35**.
  - **Python**, I dont think this needs an explanation however the version on Python could impact the code. Required version is **3.9+**.
  - **Handlandmarker** ('handlandmarker.task'), the brain of the project. Its size is roughly
    
and as such to download them, you can use:
  
```bash
pip install opencv-python
```
&
```bash
pip install mediapipe==0.10.35
```

**Important Note**: Not installing the specific version of MediapPipe or older Python versions breaks the code and will not work.

