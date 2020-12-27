import cv2 as cv
import math

listaDePuntos = []
img = cv.imread('./ejemplo.jpg')


def mousePoint(evento, x, y, flag, parametros):
    if evento == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 5, (0, 0, 255), cv.FILLED)
        listaDePuntos.append([x, y])
        print(listaDePuntos)

while True:
    cv.imshow('Imagen', img)
    cv.setMouseCallback('Imagen', mousePoint)
    if cv.waitKey(1) & 0xFF == ord('q'):
        listaDePuntos = []
        img = cv.imread('./ejemplo.jpg')





