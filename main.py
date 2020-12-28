import cv2 as cv
import math

listaDePuntos = []
img = cv.imread('./ejemplo.jpg')

def pendiente(pt1, pt2):
    return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])

def sacarAngulo():
    pt1, pt2, pt3 = listaDePuntos[-3:]
    m1 = pendiente(pt1, pt2)
    m2 = pendiente (pt1, pt3)
    angR = math.atan((m2 - m1)/(1 + (m2 * m1))) 
    angD = round(math.degrees(angR))
    print('El angulo es ' + str(angD))


def mousePoint(evento, x, y, flag, parametros):
    if evento == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 5, (0, 0, 255), cv.FILLED)
        listaDePuntos.append([x, y])
        print(listaDePuntos)

while True:
    if len(listaDePuntos) % 3 == 0 and len(listaDePuntos) != 0:
        sacarAngulo()

    cv.imshow('Imagen', img)
    cv.setMouseCallback('Imagen', mousePoint)
    if cv.waitKey(1) & 0xFF == ord('q'):
        listaDePuntos = []
        img = cv.imread('./ejemplo.jpg')





