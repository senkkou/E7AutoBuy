from tkinter import filedialog, simpledialog
from tkinter import *
import pytesseract as ocr
import subprocess
import PIL
from PIL import Image
from io import BytesIO
import time
import configparser
import ctypes
import datetime
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


def config():
    ctypes.windll.user32.MessageBoxW(0, "Select tesseract.exe file", "Setting Up", 0)
    tesseractFile = filedialog.askopenfile().name
    ctypes.windll.user32.MessageBoxW(0, "Select adb.exe file", "Setting Up", 0)
    adbFile = filedialog.askopenfile().name
    delayset = simpledialog.askfloat(" ", "Delay value (Default is 1)\nIf your emulator has bad performance set a higher value\nOpen config.ini if want to change it later")
    if delayset is None:
        delayset = 1
    configFile = open('config.ini', 'w')
    configFile.write(f'[Refresh]\ntesseractPath = {tesseractFile}\nadbPath = {adbFile}\ndelay = {delayset}')
    configFile.close()


def crashhandler(handled=""):
    logging.basicConfig(filename='crash.log')
    logging.exception(f'\n{datetime.datetime.now()}{handled}\n')
    killadb()
    ctypes.windll.user32.MessageBoxW(0, "Something went wrong, check crash.log file", "Crash Handler", 0)
    sys.exit()


Tk().withdraw()
try:
    open('config.ini', 'x')
    config()
except FileExistsError:
    pass

try:
    config = configparser.ConfigParser()
    config.read('config.ini')
    ocr.pytesseract.tesseract_cmd = config.get('Refresh', 'tesseractPath')
    adb_path = config.get('Refresh', 'adbPath')
    adb_path = f'"{adb_path}"'
    delay = config.getfloat('Refresh', 'delay')
except:
    crashhandler("\nCheck your config.ini file")

rolls = simpledialog.askinteger(" ", "Number of refreshes\nSkystones spent will be 3 times this value")
if rolls is None:
    sys.exit()
cBM = 0
MM = 0
try:
    subprocess.Popen(f"{adb_path} devices")
    print("TO STOP ANYTIME PRESS CTRL+C IN THE CONSOLE")
    time.sleep(5)
    resolution = screen()
except PIL.UnidentifiedImageError:
    crashhandler("\nProbably ADB isn't enabled on emulator")

if (resolution.size[0]/16) != (resolution.size[1]/9):
    ctypes.windll.user32.MessageBoxW(0, f"Resolution {resolution.size[0]}x{resolution.size[1]} not supported, use 16:9 aspect ratio", "Error", 0)
    killadb()
    sys.exit()
ET = str(datetime.timedelta(seconds=(rolls*11.5*delay)))[:8]
result = ctypes.windll.user32.MessageBoxW(0, f"Skystones = {3*rolls}\nRefreshes = {rolls}\nDelay = {delay}x\nEstimated time = {ET}\nTO STOP ANYTIME PRESS CTRL+C IN THE CONSOLE\nReady to start ?", "Setup", 4)
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
start = datetime.datetime.now()

try:
    for x in range(rolls + 1):
        print(f'{x}/{rolls}')
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
except KeyboardInterrupt:
    pass
except:
    crashhandler()
end = datetime.datetime.now()
goldSpent = ((184*cBM) + (280*MM))*1000
rerollResults = f'Covenant Bookmark = {5*cBM}\nMystic Medals = {50*MM}\nGold Spent = {goldSpent}\n'
log = open("logs.txt", "a")
log.write(f'Started at {start}\nEnded at {end}\nTime elapsed: {end-start}\nRefreshes = {x}\nSkystones spent = {3*x}\n{rerollResults}\n')
log.close()
killadb()
ctypes.windll.user32.MessageBoxW(0, rerollResults, "Results", 0)
