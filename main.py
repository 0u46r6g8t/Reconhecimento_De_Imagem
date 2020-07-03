// Importação das bibliotecas necessárias

import cv2 // Biblioteca para utilizar os recurso da câmera e fazer o reconhecimento 
import numpy as np 
import biblioteca as b
import carrinho // Importa o os métodos do arquivo de controle direita, esquerda, frente e parar

cap = cv2.VideoCapture(0)
_, frame = cap.read()
tela = b.Tela(frame)

try:
  while True: // Laço responsável pela execução até que haja algum erro ou 
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_green = np.array([45, 100, 80])
    high_green = np.array([85, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)

    l = cv2.findContours(green_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if (len(l[1]) == 0):
      print("parado")
    else:
      v = l[1][0][0][0][0]

    if(v < tela.D1):
      print("esquerda")
      esquerda()

    elif(v > tela.D2):
      print("direita")
      direita()

    elif(v < tela.D2):
      print("frente")
      frente()

    else:
      print("Parado")
      parado()

  green = cv2.bitwise_and(frame, frame, mask=green_mask)
except KeyboardInterrupt as e:
  print("")
except as error:
  print("Error: {}".format(error))
