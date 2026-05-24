# Basic Hand-Tracker using Python.
A very small and basic python program to control a drone or aerial device using hand gestures shown to the program via CV2.

# Developers note:
This github post/project is first of many to come and hopefully not the last. Therefore I hope the readers of this stay updated with my profile because this the seed taken from a fruit. The seed that grows into a huge fruit tree and lead to more seeds. I hope you understand this Shakespeare-wannabe message. Personally, I think this code was too simple to post but I have to start somewhere... right? ***Read the DISCLAIMER.md before attempting to use or modify the code.***

# Requirements:
This project requires:
  - **OpenCV** ('opencv-python'), which handles the video footage and image processing.
  - **Google's MediaPipe** ('mediapipe'), which does most of the heavy lifting by using Google's Open Source high fidelity hand tracking and finger detection module. Required version is **0.10.35**.
  - **Python**, I dont think this needs an explanation however the version on Python could impact the code. Required version is **3.9+**.
  - **Handlandmarker** ('handlandmarker.task'), the brain of the project. Its size is roughly 7.5 MB and occupies most of the projects storage.
    
To download the Python modules, you can use:
  
```bash
pip install opencv-python
```
&
```bash
pip install mediapipe==0.10.35
```

**Important Note**: Not installing the specific version of MediapPipe or using older Python versions breaks the code and will not work.

# Credits:
- **Claude AI by Anthropic**, used to generate, teach and help to debug and fix lines of code.
- **Gemini by Google**, used to teach me how to create this README and DISCLAIMER file and its features along with choosing the best fitting licence.
- **VSCode**, used to write the code. (obviously)
- **Me**, of course, where I wrote 40% (generous btw) of the lines of code and main debuging and tester.

# Features:
- This code includes various hand-gestures to control a drone/aerial device.
- All current gestures are as follows:
  1. **Double Open Hand** facing the camera --> POWER ON
  2. **Double Closed fists** facing the camera --> POWER OFF
  3. **Both Hands tilting away from each other** --> UP
  4. **Both Hands tilting towards each other** --> DOWN
  5. **Left Hand Open and Right Hand Closed** --> LEFT
  6. **Left Hand Closed and Right Hand Open** --> RIGHT
  7. **One Hand with Index Finger pointing up** --> 360
- Gestures 3-7 are printed numerically for convenience.
  
# Tests and debugging:
- This project has been tested multiple times however if any new problems arise (in the current version of code i.e. unedited) then please feel free to contact me or fix it by yourself and send me the fixed version.
- As this project was built in certain stages, problems occured almost right after adding a new gesture or line of code so many lessons were learnt during those tests lol.
- The stages I mentioned were basically:
  1. Setting up OpenCV.
  2. Getting it to work.
  3. Changing color format. (only 1 line but that line confused me alot and idk y)
  4. Adding MediaPipe (where the first major issue arose).
  5. Adding Gestures (where most issues occured).
  6. Deployment.
- **Claude AI** was especially helpful during debuging as most of the issues that arise aren't code issues but a logic issues, so where the problems root from needed to be highlighted and **Claude** helps with that.
