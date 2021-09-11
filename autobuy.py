import pytesseract as ocr
import subprocess
from PIL import Image
import sys
from io import BytesIO
import time
import configparser
import ctypes
from datetime import datetime
import logging


def click(x, y):
    subprocess.Popen(f"{adb_path} shell input tap {x} {y}")


def screen():
    screen_bytes = subprocess.Popen(f"{adb_path} exec-out screencap -p", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    img_bytes = screen_bytes.stdout.read()
    screenshot = Image.open(BytesIO(img_bytes))
    return screenshot


def swipe(x1, y1, x2, y2):
    subprocess.Popen(f"{adb_path} shell input touchscreen swipe {x1} {y1} {x2} {y2}")


def reroll():
    time.sleep(1*delay)
    click(rbx, rby)
    time.sleep(1*delay)
    click(rbx, rby)
    time.sleep(1*delay)
    click(rbcx, rbcy)
    time.sleep(1*delay)
    click(rbcx, rbcy)
    time.sleep(2*delay)


def buy(slot):
    time.sleep(1 * delay)
    if slot == 5:
        y = slot5
    elif slot == 4:
        y = slot4
    else:
        swipe(swipex, swipey2, swipex, swipey1)
        time.sleep(2 * delay)
        if slot == 3:
            y = slot3
        elif slot == 2:
            y = slot2
        elif slot == 1:
            y = slot1
        elif slot == 0:
            y = slot0

    time.sleep(2 * delay)
    click(slotb, y)
    time.sleep(1 * delay)
    click(slotb, y)
    time.sleep(1 * delay)
    click(slotcx, slotcy)
    time.sleep(1 * delay)
    click(slotcx, slotcy)

    time.sleep(2 * delay)
    swipe(swipex, swipey1, swipex, swipey2)
    time.sleep(4 * delay)


def killadb():
    subprocess.Popen(r'taskkill /IM "adb.exe" /F')

try:
    config = configparser.ConfigParser()
    config.read('config.ini')
    ocr.pytesseract.tesseract_cmd = config.get('Refresh', 'tesseractPath')
    adb_path = config.get('Refresh', 'adbPath')
    adb_path = f'"{adb_path}"'
    rolls = config.getint('Refresh', 'number_of_refresh')
    delay = config.getint('Refresh', 'delay')
    cBM = 0
    MM = 0
    subprocess.Popen(f"{adb_path} devices")
    time.sleep(5)
    resolution = screen()
    if (resolution.size[0]/16) != (resolution.size[1]/9):
        ctypes.windll.user32.MessageBoxW(0, f"Resolution {resolution.size[0]}x{resolution.size[1]} not supported, use 16:9 aspect ratio", "Error", 0)
        killadb()
        sys.exit()
    result = ctypes.windll.user32.MessageBoxW(0, f"Skystones = {3*rolls}\nRefreshes = {rolls}\nReady to start ?", "Setup", 4)
    if result != 6:
        killadb()
        sys.exit()

    ratio = resolution.size[0]/1280

    rbx = int(230*ratio)
    rby = int(660*ratio)
    rbcx = int(740*ratio)
    rbcy = int(440*ratio)
    slotb = int(1150*ratio)
    slot0 = int(160*ratio)
    slot1 = int(300*ratio)
    slot2 = int(450*ratio)
    slot3 = int(595*ratio)
    slot4 = int(530*ratio)
    slot5 = int(670*ratio)
    slotcx = int(750*ratio)
    slotcy = int(510*ratio)
    cropulx = int(680*ratio)
    cropul0 = int(90*ratio)
    cropul1 = int(232*ratio)
    cropul2 = int(375*ratio)
    cropul3 = int(525*ratio)
    cropul4 = int(460*ratio)
    cropul5 = int(605*ratio)
    cropbrx = int(1000*ratio)
    cropbr0 = int(180*ratio)
    cropbr1 = int(332*ratio)
    cropbr2 = int(475*ratio)
    cropbr3 = int(625*ratio)
    cropbr4 = int(550*ratio)
    cropbr5 = int(695*ratio)
    swipex = int(1000*ratio)
    swipey1 = int(575*ratio)
    swipey2 = int(250*ratio)

    for x in range(rolls + 1):
        images = []
        ss = screen()

        images.append(ss.crop((cropulx, cropul0, cropbrx, cropbr0)))
        images.append(ss.crop((cropulx, cropul1, cropbrx, cropbr1)))
        images.append(ss.crop((cropulx, cropul2, cropbrx, cropbr2)))
        images.append(ss.crop((cropulx, cropul3, cropbrx, cropbr3)))

        time.sleep(1 * delay)
        swipe(swipex, swipey1, swipex, swipey2)
        time.sleep(2 * delay)
        ss = screen()
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
    killadb()
    ctypes.windll.user32.MessageBoxW(0, rerollResults, "Results", 0)
except:
    logging.basicConfig(filename='crash.log')
    logging.exception(f'\n{datetime.now()}\n\n')
    killadb()
    ctypes.windll.user32.MessageBoxW(0, "Something went wrong, check crash.log file", "Crash Handler", 0)
