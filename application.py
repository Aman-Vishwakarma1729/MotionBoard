import cv2
import cvzone
from time import time
from cvzone.HandTrackingModule import HandDetector
from screeninfo import get_monitors
import warnings
warnings.filterwarnings('ignore')

screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", screen_width, screen_height)

# Start Video Capture
cap = cv2.VideoCapture(0)  # Adjust the camera
cap.set(3, screen_width)
cap.set(4, screen_height)

detector = HandDetector(detectionCon=0.8)

# Keyboard Layout
keys = [
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "<"],
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
    ["Space", "Enter"]
]
finalText = ""

class Button:
    def __init__(self, pos, text, size=[60, 60]):  # Adjusted size of the buttons
        self.pos = pos
        self.size = size
        self.text = text

def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]), 10, rt=4)
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 255, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 5, y + 30), cv2.FONT_HERSHEY_PLAIN, 2, (150, 150, 150), 2)
    return img

# Create button list
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        if key == "Space":
            buttonList.append(Button([450, 80 * i + 90], key, size=[160, 60]))  # Adjusted size for space button
        elif key == "Enter":
            buttonList.append(Button([650, 80 * i + 90], key, size=[160, 60]))  # Adjusted position for enter button
        else:
            buttonList.append(Button([80 * j + 220, 100 * i + 10], key))

# Variables to manage debounce and stability effect
lastKeyPressed = None
lastPressTime = 0
pressCooldown = 0.5  # Time in seconds
stableTime = 0.2  # Time in seconds
startStableTime = None
currentButton = None

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break
    
    hands, img = detector.findHands(img, draw=True, flipType=True)
    img = drawAll(img, buttonList)

    if hands:
        lmListHand = hands[0]['lmList']
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lmListHand[8][0] < x + w and y < lmListHand[8][1] < y + h:
                if currentButton != button.text:
                    startStableTime = time()
                    currentButton = button.text

                if currentButton == button.text:
                    if startStableTime is not None and time() - startStableTime > stableTime:
                        cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (130, 80, 70), cv2.FILLED)
                        cv2.putText(img, button.text, (x + 10, y + 40), cv2.FONT_HERSHEY_PLAIN, 2, (200, 200,200), 2)

                        l, _, _ = detector.findDistance((lmListHand[8][0], lmListHand[8][1]), 
                                                        (lmListHand[12][0], lmListHand[12][1]), img)

                        currentTime = time()
                        if l < 30 and (lastKeyPressed != button.text or (currentTime - lastPressTime) > pressCooldown):
                            #print(f"Key Pressed: {button.text}")
                            cv2.rectangle(img, button.pos, (x + w, y + h), (230,50,230), cv2.FILLED)
                            cv2.putText(img, button.text, (x + 10, y + 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                            if button.text == "<":  # Handle backspace
                                finalText = finalText[:-1]
                            elif button.text == "Space":  # Handle space
                                finalText += " "
                            elif button.text == "Enter":  # Handle enter
                                print(f"{finalText}")
                                finalText = ""  # Clear the text after printing
                            else:
                                finalText += button.text
                            lastKeyPressed = button.text
                            lastPressTime = currentTime
                            startStableTime = None  # Reset stable time after a key press

    else:
        currentButton = None  # Reset currentButton when no hands are detected

    # Draw text box
    #cv2.rectangle(img, (100, 550), (1150, 600), (175, 0, 175), cv2.FILLED)  # Adjusted text box position and size
    cv2.putText(img, finalText, (50, 600), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
