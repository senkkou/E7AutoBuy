# E7AutoBuy

Auto refreshes secret shop and buy all Covenant Bookmarks and Mystic Medals  
  
# v2.0
-Now you can use your PC while AutoBuy is running  
-Your monitor resolution doesn't matter anymore  
  
## Get Started:  
1-Install Tesseract OCR https://github.com/UB-Mannheim/tesseract/wiki  
2-Download platform-tools https://dl.google.com/android/repository/platform-tools-latest-windows.zip  
3-Open config.ini  
4-Set tesseractPath to your tesseract.exe file (from Tesseract OCR)  
5-Set adbPath to your adb.exe file (from platform-tools)  
6-Make sure your game is in english  
7-Enable ADB on your emulator  
<details><summary>Show</summary>  
  
![adb](https://user-images.githubusercontent.com/54269537/132781083-e40bd44b-e551-4b84-9da4-586aa519a937.png)  
  
</details>  
  
   
 ### How to use:  
1-In config.ini set the number of refreshes you want AutoBuy to do, the number of skystones spent will be 3 times this value.  
2-Delay = 1 is the default speed, if you are using a PC with bad performance try to increase the delay to run it slowly.   
4-Finish your dispatch mission or start long ones (So the window doesnt pop up during shop reroll).  
5-Change chat to a empty channel (To avoid chat pop ups).    
6-Start the program.  
7-Open secret shop.  
8-Confirm program window.  
  
Now you can minimize your emulator and console window and freely use your PC while AutoBuy is running.  
When it finishes, a window will pop up and shows the results and a log file will be saved in AutoBuy directory.  
  
### Python and packages used to compile:  
-python 3.8.11  
-pytesseract 0.3.8  
-pillow 8.3.1  
  
  

<details><summary>v1.0 OLD</summary>  
  
## Get Started:  
1-Install Tesseract OCR https://github.com/UB-Mannheim/tesseract/wiki  
2-Open config.ini  
3-Make sure tesseractPath is the same you installed tesseract-ocr  
4-Make sure your game is in english  
  
### How to use:  
1-In config.ini set the number of refreshes you want the bot to do, the number of skystones spent will be 3 times this value  
2-Delay = 1 is the default speed, if you are using a PC with bad performance try to increase the delay to run it slowly  
3-Use your emulator with maximized window (Like the images bellow) and it must be on your main monitor  
4-Finish your dispatch mission or start long ones. (So the window doesnt pop up during shop reroll)  
5-Change chat to a empty channel  
6-Start the program  
7-Open secret shop  
8-Confirm program window.  
  
Additional notes:  
It will only work if your screen resolution is in presets.ini, by default 1280x720, 1920x1080 and 2560x1080  
if you use any other resolution change to one of the three above or do your own configuration and write in the file.  
  
### Python and packages used to compile:  
-python 3.8.11  
-pytesseract 0.3.8  
-pillow 8.3.1  
-pyautogui 0.9.53  
  
 ### Setting Up your own resolution:  
 You can edit the presets.ini to add your own resolution, you just need to type for each variable the pixel's coordinates for you resolution.  
 Bellow are some images showing where you should be getting your cordinates from, for each variable.  
 
 Ps: cropubr in images were supose to be cropbr, but i'm too lazy to redo the screens.  
   
 <details><summary>Show Images</summary>  
  
Open up each image to see better the marked pixel  

![1](https://user-images.githubusercontent.com/54269537/131053834-5c2f2efb-09cc-44f0-8692-d1758e5252b7.png)  
  
![2](https://user-images.githubusercontent.com/54269537/131054917-0ba0246b-ad83-4f32-ad44-b41c0cd866a5.png)  
  
![3](https://user-images.githubusercontent.com/54269537/131054932-3c4f4c5e-1f61-4b22-80b9-d96fa14c02ad.png)  
   
![4](https://user-images.githubusercontent.com/54269537/131054955-8722a72b-cfa0-4246-92e9-0cc37cbd1db9.png)

</details>  
</details>  
  
## Warning  
For the first time, before you try it with a high number of rerolls, refresh it manually until a covenant or mystic shows up.  
Then set the number of reroll to something like 3 just to test if it is working fine.
