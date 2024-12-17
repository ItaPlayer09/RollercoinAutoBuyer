import os
import time
import pyautogui as py
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

url = input("Please give the item url: ")
targetValue = input("Please give a target value: ")

screenshot_area = (, , , )

def MouseClick(coords):
    py.click(coords)

def CheckValue():
    screen = py.screenshot(region=screenshot_area)
    screen.save("img.png")
    img = Image.open("img.png")
    output = pytesseract.image_to_string(img)
    print(output)
    return output

while True:
    if CheckValue() == targetValue:
        MouseClick((100, 100))
        print("bought item")
    time.sleep(0.1)
