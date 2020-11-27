import cv2
import numpy
import random
import pyautogui
import time
import keyboard
from PIL import ImageGrab


class yonler:
    def ileri(self,hesaplanan_saniye_degeri):
        pyautogui.keyDown("w")
        time.sleep(hesaplanan_saniye_degeri)
        pyautogui.keyUp("w")
    def sag(self,hesaplanan_saniye_degeri):
        pyautogui.keyDown("d")
        time.sleep(hesaplanan_saniye_degeri)
        pyautogui.keyUp("d")
    def sol(self,hesaplanan_saniye_degeri):
        pyautogui.keyDown("a")
        time.sleep(hesaplanan_saniye_degeri)
        pyautogui.keyUp("a")

def egim_donustur(egim):
    keyboard.press("w")
    time.sleep(0.01)

    if egim > 0 and egim < 30 :
        if egim > 0 and egim <= 10 :
            keyboard.press("d")
            keyboard.press("w")
            time.sleep(0.003)
            keyboard.release("w")
            keyboard.release("d")

        elif egim > 10 and egim <= 20 :
            keyboard.press("d")
            keyboard.press("w")
            time.sleep(0.005)
            keyboard.release("w")
            keyboard.release("d")

        elif egim > 20 and egim <= 30 :
            keyboard.press("d")
            keyboard.press("w")
            time.sleep(0.007)
            keyboard.release("w")
            keyboard.release("d")
        elif egim > 30 and egim <= 40 :
            keyboard.press("d")
            keyboard.press("w")
            time.sleep(0.009)
            keyboard.release("w")
            keyboard.release("d")


    if egim < 0 and egim > -30 :
        if egim < 0 and egim >= -10:
            keyboard.press("a")
            keyboard.press("w")
            time.sleep(0.003)
            keyboard.release("w")
            keyboard.release("a")

        if egim < -10 and egim >= -20:
            keyboard.press("a")
            keyboard.press("w")
            time.sleep(0.005)
            keyboard.release("w")
            keyboard.release("a")

        if egim < -20 and egim >= -30:
            keyboard.press("a")
            keyboard.press("w")
            time.sleep(0.007)
            keyboard.release("w")
            keyboard.release("a")
        if egim < -30 and egim >= -40:
            keyboard.press("a")
            keyboard.press("w")
            time.sleep(0.009)
            keyboard.release("w")
            keyboard.release("a")



def hesaplama(lines):
    if type(lines) is not None:
        for cizgi in lines:
            kordinatlar = cizgi[0]
            x1 = kordinatlar[0]
            x2 = kordinatlar[2]
            y1 = kordinatlar[1]
            y2 = kordinatlar[3]
            for cizgi1 in lines:
                kordinatlar1 = cizgi1[0]
                xx1 = kordinatlar1[0]
                xx2 = kordinatlar1[2]
                yy1 = kordinatlar1[1]
                yy2 = kordinatlar1[3]

                aradaki_mesafe = ((x1-xx1)**2 + (y1 - yy1)**2)**(1/2)
                aradaki_mesafe1 = ((x2 - xx2) ** 2 + (y2 - yy2) ** 2) ** (1 / 2)

                if (xx1 - xx2) != 0 and (x1 - x2) != 0:
                    egim = (y2 - y1) / (x1 - x2)
                    egim1 = (yy2 - yy1) / (xx1 - xx2)
                    if abs(egim) > 40:
                        egim = 40
                        egim1 = 40
                else:
                    egim = 40
                    egim1 = 40


                if abs(aradaki_mesafe - aradaki_mesafe1) < 10 and aradaki_mesafe != 0 and aradaki_mesafe < 20 and abs(egim) > 0.5 and (abs(egim) - abs(egim1)) < 2 :
                    #print(egim)
                    egim_donustur(egim)
                    X1 = 50
                    Y1 = 450
                    Y2 = 150
                    X2 = int(abs(Y1-Y2)/ egim +X1)
                    XX1  =250
                    YY1 = 450
                    YY2 = 250
                    XX2 = int(abs(YY1-YY2)/ egim +XX1)
                    cv2.line(ekran1,(X1,Y1),(X2,Y2),(0,255,0),5)
                    cv2.line(ekran1, (XX1, YY1), (XX2, YY2), (0, 255, 0), 5)


print("10 saniye sonr başlıyor")
time.sleep(10)
while True:
    last_time = time.time()
    ekran = numpy.array(ImageGrab.grab(bbox=(0, 0, 1000, 700)))
    ekran1 = ekran[200:450,150:550]
    gri = cv2.cvtColor(ekran, cv2.COLOR_BGR2GRAY)
    #ana_resim = cv2.cvtColor(ekran, cv2.COLOR_BGR2RGB)
    resim = gri[150:700, 350:650]
    #kernel = numpy.ones((7, 15), dtype=numpy.uint8)
    canny = cv2.Canny(resim, 200, 200)
    #closing = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
    blur = cv2.GaussianBlur(canny, (3, 3), 0)
    minLineLength = 15
    maxLineGap = 10
    lines = cv2.HoughLinesP(blur, 1, numpy.pi / 180, 180, 2, minLineLength, maxLineGap)

    cv2.imshow("closing",ekran1)
    #keyboard.press("w")

    if lines is not None :
        hesaplama(lines)
        ekran1 = cv2.pyrDown(ekran1)
        cv2.imshow("line", ekran1)
    else:
        pass
    print("zaman geçti = {}".format(time.time() - last_time))

    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
