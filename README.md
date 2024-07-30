# <div align="center">MotionBoard: Typing Powered by Hand Movements</div>
<div align="center">
  <img src="readme_data/poster.png" alt="Designer" width="500"/>
</div>

## Table of content
--------------
1. [Introduction](#introduction)
2. [Features](#features)
4. [How it works](#how-it-works)
4. [Demo](#demo)
5. [Usage](#usage)
6. [How to use](#how-to-use)
7 . [Customization](#customization)

## Introduction
---------------
This project implements a virtual keyboard using computer vision techniques. The keyboard is designed to detect and track hand movements to simulate typing on a physical keyboard. This can be particularly useful for accessibility, innovative interfaces, and contactless interaction systems.

## Features
-----------
* **Hand Tracking:** Utilizes the google MEDIAPIPE to detect and track hand movements.
* **Customizable Keyboard Layout:** Supports different keyboard layouts with adjustable button sizes.
* **Stable Key Press Detection:** Ensures stable and accurate key presses using a debouncing mechanism.
* **Real-time Feedback:** Provides visual feedback on key presses with highlighted buttons.
* **Special Keys Support:** Includes functionality for space, backspace, and enter keys.

## How it works
----------------
* **Camera Capture:** Captures live video feed from the webcam.
* **Hand Detection:** Uses cvzone.HandTrackingModule to detect hand and finger positions.
* **Key Press Detection:** Determines which key is pressed based on the position of the index finger.
* **Debouncing Mechanism:** Ensures stable key presses by requiring the finger to remain over the key for a specified duration.
* **Special Keys:** Handles space, backspace, and enter keys appropriately.

## Demo
--------
**Watch the demo video to see the virtual keyboard in action:** [Demo Video](Demo_use_video.mp4)

## Usage
---------
* git clone the repository
* pip install -r requirements.txt
* python application.py

## How to use
---------------
* Position your hand in front of the webcam.
* Move your index finger to hover over the desired key.
* Press the key by bringing your finger close to the camera.
* Use the backspace key ("<") to delete characters.
* Use the space key ("Space") to add spaces.
* Use the enter key ("Enter") to submit the typed text.

## Customization
----------------
* You can customize the keyboard layout by modifying the keys variable in the script:
keys = [
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "<"],
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
    ["Space", "Enter"]
]

