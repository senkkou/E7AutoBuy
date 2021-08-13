import pytesseract as ocr
from PIL import Image
import pyautogui as macro
import time
import ctypes
import configparser
from datetime import datetime
import sys

config = configparser.ConfigParser()
config.read('config.ini')
ocr.pytesseract.tesseract_cmd = config.get('Refresh', 'tesseractPath')
rolls = config.getint('Refresh', 'number_of_refresh')
delay = config.getint('Refresh', 'delay')

#allowedResolution = "2560x1080 1920x1080 1280x720"
screensize = f'{ctypes.windll.user32.GetSystemMetrics(0)}x{ctypes.windll.user32.GetSystemMetrics(1)}'
#if screensize not in allowedResolution:
#    ctypes.windll.user32.MessageBoxW(0, f"Resolution {screensize} not supported", "Error", 0)
#    sys.exit()

presets = configparser.ConfigParser()
presets.read('presets.ini')
try:
    cenx = int(presets.get(screensize, 'cenx'))
    ceny = int(presets.get(screensize, 'ceny'))
    rbx = int(presets.get(screensize, 'rbx'))
    rby = int(presets.get(screensize, 'rby'))
    rbcx = int(presets.get(screensize, 'rbcx'))
    rbcy = int(presets.get(screensize, 'rbcy'))
    slotb = int(presets.get(screensize, 'slotb'))
    slot0 = int(presets.get(screensize, 'slot0'))
    slot1 = int(presets.get(screensize, 'slot1'))
    slot2 = int(presets.get(screensize, 'slot2'))
    slot3 = int(presets.get(screensize, 'slot3'))
    slot4 = int(presets.get(screensize, 'slot4'))
    slot5 = int(presets.get(screensize, 'slot5'))
    slotcx = int(presets.get(screensize, 'slotcx'))
    slotcy = int(presets.get(screensize, 'slotcy'))
    cropulx = int(presets.get(screensize, 'cropulx'))
    cropul0 = int(presets.get(screensize, 'cropul0'))
    cropul1 = int(presets.get(screensize, 'cropul1'))
    cropul2 = int(presets.get(screensize, 'cropul2'))
    cropul3 = int(presets.get(screensize, 'cropul3'))
    cropul4 = int(presets.get(screensize, 'cropul4'))
    cropul5 = int(presets.get(screensize, 'cropul5'))
    cropbrx = int(presets.get(screensize, 'cropbrx'))
    cropbr0 = int(presets.get(screensize, 'cropbr0'))
    cropbr1 = int(presets.get(screensize, 'cropbr1'))
    cropbr2 = int(presets.get(screensize, 'cropbr2'))
    cropbr3 = int(presets.get(screensize, 'cropbr3'))
    cropbr4 = int(presets.get(screensize, 'cropbr4'))
    cropbr5 = int(presets.get(screensize, 'cropbr5'))
except:
    ctypes.windll.user32.MessageBoxW(0, f"Resolution {screensize} not supported", "Error", 0)
    sys.exit()

def buy(slot):
    time.sleep(1*delay)
    if slot == 5:
        y = slot5
    elif slot == 4:
        y = slot4
    else:
        macro.click(cenx, ceny)
        time.sleep(1*delay)
        macro.scroll(250)
        time.sleep(2*delay)
        if slot == 3:
            y = slot3
        elif slot == 2:
            y = slot2
        elif slot == 1:
            y = slot1
        elif slot == 0:
            y = slot0

    time.sleep(2*delay)
    macro.click(slotb, y)
    time.sleep(1*delay)
    macro.click(slotb, y)
    time.sleep(1*delay)
    macro.click(slotcx, slotcy)
    time.sleep(1*delay)
    macro.click(slotcx, slotcy)

    time.sleep(2*delay)
    macro.click(cenx, ceny)
    time.sleep(1*delay)
    macro.scroll(-250)
    time.sleep(4*delay)

def reroll():
    time.sleep(1*delay)
    macro.click(rbx, rby)
    time.sleep(1*delay)
    macro.click(rbx, rby)
    time.sleep(1*delay)
    macro.click(rbcx, rbcy)
    time.sleep(1*delay)
    macro.click(rbcx, rbcy)
    time.sleep(1*delay)

cBM = 0
MM = 0
result = ctypes.windll.user32.MessageBoxW(0, f"Skystones = {3*rolls}\nRefreshes = {rolls}\nResolution = {screensize}\nReady to start ?", "Setup", 4)
if result != 6:
    sys.exit()
for x in range(rolls+1):
    images = []
    ss = macro.screenshot()

    images.append(ss.crop((cropulx, cropul0, cropbrx, cropbr0)))
    images.append(ss.crop((cropulx, cropul1, cropbrx, cropbr1)))
    images.append(ss.crop((cropulx, cropul2, cropbrx, cropbr2)))
    images.append(ss.crop((cropulx, cropul3, cropbrx, cropbr3)))

    time.sleep(1*delay)
    macro.click(cenx, 500)
    time.sleep(1*delay)
    macro.scroll(-250)
    time.sleep(2*delay)
    ss = macro.screenshot()
    images.append(ss.crop((cropulx, cropul4, cropbrx, cropbr4)))
    images.append(ss.crop((cropulx, cropul5, cropbrx, cropbr5)))

    ocrimage = []
    for im in images:
        ocrimage.append(ocr.image_to_string(im))

    count = 0
    slots = []
    for text in ocrimage:
        if "Covenant Bookmarks" in text:
            slots.append(count)
            cBM += 1
        elif "Mystic Medals" in text:
            slots.append(count)
            MM += 1
        count += 1

    if slots:
        for slot in slots:
            buy(slot)

    if x == rolls:
        break
    reroll()


goldSpent = ((184*cBM) + (280*MM))*1000
rerollResults = f'Covenant Bookmark = {5*cBM}\nMystic Medals = {50*MM}\nGold Spent = {goldSpent}\n'

log = open("logs.txt", "a")
log.write(f'{datetime.now()}\nSkystones spent = {3*rolls}\n{rerollResults}\n')
log.close()

ctypes.windll.user32.MessageBoxW(0, rerollResults, "Results", 0)

