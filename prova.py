import os
import time
import pyautogui as py
import pytesseract
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

url = input("Please give the item url: ")
targetValue = input("Please give a target value: ")

screenshot_area = (1393, 448, 168, 27)

def MouseClick(coords):
    py.click(coords)

def CheckValue():
    screen = py.screenshot(region=screenshot_area)
    screen.save("img.png")
    img = Image.open("img.png")
    output = pytesseract.image_to_string(img)
    output = output[:-9]
    print(output)
    print(targetValue)
    return output
    if output == targetValue:
        print("target price reached")

while True:
    time.sleep(0.1)
    CheckValue()
