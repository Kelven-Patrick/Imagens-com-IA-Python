# Script em Python
# Autor: Kelven Patrick Novaes Barbosa
# Data: 20-08-2024
# Descrição: Esse codigo feito em Pyton capitura a imagem da webcam com IA.

# importa a biclioteca 
import cv2
from cvzone.HandTrackingModule import HandDetector

# varieaveis
webcan = cv2.VideoCapture(0)
rastreador = HandDetector(detectionCon=0.8, maxHands=2)

# loop para ativação e leitura da webcam
while True:
    sucesso, imagem = webcan.read()
    cordenadas, image_maos = rastreador.findHands(imagem)
    
    # imprime as cordenadas
    print(cordenadas)

    cv2.imshow("Projeto 4 - IA", imagem)

    if cv2.waitKey(1) != -1:
        break

# libera a webcam
webcan.release()
cv2.destroyAllWindows()
