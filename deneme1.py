import cv2
import numpy
import random

def hesaplama(lines):
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
            m1 = (xx1 - xx2)
            m2 = (x1 - x2)
            if m1 == 0 or m2 == 0:
                m1 = 1
                m2 = 1
            egim = (y1 - y2) / m2
            egim1 = (yy1 - yy2) / m1

            if abs(aradaki_mesafe - aradaki_mesafe1) < 3 and aradaki_mesafe != 0 and aradaki_mesafe < 20 and abs(egim) > 0.5 :
                #print(aradaki_mesafe,aradaki_mesafe1)
                koseler = numpy.array([[x1, y1], [x2, y2], [xx2, yy2],[xx1,yy1]])
                cv2.fillPoly(resim, [koseler],(0,0,255))
                #print("paralel",cizgi,cizgi1)
        #print("eğimler",egim1,egim)

resim = cv2.imread("oyundan3.jpg")
resim = resim[50:700,350:650]
kernel = numpy.ones((7,15), dtype=numpy.uint8)

gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gri,200,300)
closing = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)
blur = cv2.GaussianBlur(canny,(9,7),0)
minLineLength = 1
maxLineGap = 10
lines = cv2.HoughLinesP(blur,1,numpy.pi/180,180,2,minLineLength,maxLineGap)

for cizgi in lines:
    a = random.randint(0,255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    kordinatlar = cizgi[0]
    cv2.line(resim,(kordinatlar[0],kordinatlar[1]),(kordinatlar[2],kordinatlar[3]),(a,b,255),1,cv2.LINE_AA)
    #print(cizgi)

#print(len(lines))
cv2.imshow("sade",resim)
hesaplama(lines)
#resim = cv2.pyrDown(resim)
cv2.imshow("line",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()