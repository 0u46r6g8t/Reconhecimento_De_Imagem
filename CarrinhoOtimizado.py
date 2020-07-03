#! /usr/bin/env python3

# Importando as Bibliotecas

from gpiozero import PWMOutputDevice
import time

# from opencv import cv2

#-------------------------------------------------
# ->> Nome do grupo: Gustavo S./Luis R. e Lucas F.
# ->> Matéria: Arquitetura de Computadores 
# ->> Professor/Orientador: Itamar Iliuk
# ->> Periódo: 3° Semestre Regular
#-------------------------------------------------

# Configurando as portas GPIO
IN1 = 26 # Motor 1°
IN2 = 19 # Motor 2°
IN3 = 13 # Motor 1°
IN4 = 6 # Motor  2°

# Inicializando os pinos para que possam ser ativados/desativados

# Motor Primáio

Frente_Esq = PWMOutputDevice(IN1, True, 0, 1000)
Frente_Dir = PWMOutputDevice(IN3, True, 0, 1000)

# Motor Secundário

Re_Dir = PWMOutputDevice(IN2, True, 0, 1000)
Re_Esq = PWMOutputDevice(IN4, True, 0, 1000)


# Criando as funções responsáveis por controlar os motores

def frente():
	Frente_Esq.value = 1.0
	Frente_Dir.value = 1.0
	Re_Esq.value = 0
	Re_Dir.value = 0

def direita():
	Frente_Dir.value = 1.0
	Frente_Esq.value = 0
	Re_Dir.value = 1.0
	Re_Esq.value = 0

def esquerda():
	Frente_Dir.value = 0
	Re_Esq.value = 1.0
	Frente_Esq.value = 1.0
	Re_Dir.value = 0


## Quando for utilizar as funções de direção como
## 		-> Direita 
## 				ou
##		-> Esquerda
## Coloque um Sleep de 5 segundos, pois irá virar corretamente no sentido desejado
######################################################################################
## Bibliotecas a serem instaladas 
#
#	-> °gpiozero
#
## Command: sudo pip install gpiozero 