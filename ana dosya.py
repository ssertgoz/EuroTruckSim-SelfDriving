import cv2
import numpy
from PIL import ImageGrab
import time
import pyautogui
import sys
import math

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





def cizgi_bul(dst):

        cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
        cdstP = numpy.copy(cdst)



        linesP = cv2.HoughLinesP(dst, 1, numpy.pi / 180, 180, None, 100, 2)

        if linesP is not None:
            for i in range(0, len(linesP)):
                l = linesP[i][0]
                cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv2.LINE_AA)


        return cdstP




def resim_isleme(ana_resim):
    kernel = numpy.ones((3,3), dtype=numpy.uint8)
    islenmis_resim = cv2.cvtColor(ana_resim,cv2.COLOR_BGR2GRAY)
    islenmis_resim = cv2.Canny(islenmis_resim,threshold1=200,threshold2=200,edges=None,apertureSize=3)
    islenmis_resim = cv2.dilate(islenmis_resim, kernel, iterations=1)
    #islenmis_resim = cv2.GaussianBlur(islenmis_resim,(1,1),1)
    islenmis_resim = maskeleme(islenmis_resim)

    #                      cizgi bulma

    islenmis_resim = cizgi_bul(islenmis_resim)
    return islenmis_resim



def maskeleme(resim):
    koseler = numpy.array([[0,0],[0,1000],[700,1000],[600,700],[600,50],[400,50],[400,700],[0,700]])
    maske = numpy.zeros_like(resim)
    cv2.fillPoly(maske,[koseler],255)
    maskelenmis = cv2.bitwise_and(resim,maske)
    return maskelenmis

def cizgi_ciz(img,cizgiler):
    try:
        for cizgi in cizgiler:
            kordinatlar = cizgi[0]
            cv2.line(img,(kordinatlar[0],kordinatlar[1]),(kordinatlar[2],kordinatlar[3]),(0,0,255),11)
    except:
        pass







while True:
    #last_time = time.time()
    ekran = numpy.array(ImageGrab.grab(bbox=(0,0, 1000, 700)))
    ana_resim = cv2.cvtColor(ekran, cv2.COLOR_BGR2RGB)
    islenmis = resim_isleme(ana_resim)
    resim = cv2.pyrDown(islenmis)
    resim = cv2.pyrDown(resim)
    cv2.imshow("resim",resim)

    #print("loopta bu kadarzaman geçti = {}".format(time.time()-last_time))




    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break




