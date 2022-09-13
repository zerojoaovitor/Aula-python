# Bibliotecas

import RPi.GPIO as GPIO
import time

# Portas GPIO

led1 = 12   # vermelho
led2 = 16   # amarelo
led3 = 18   # verde

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

GPIO.setwarnings(False)

while True: #loop infinito
    GPIO.output(led1, 1)   #led vermelho 10s ligado
    time.sleep(10)
    GPIO.output(led1, 0)
    time.sleep(1)

    GPIO.output(led2, 1)  # led amarelo 2s ligado
    time.sleep(2)
    GPIO.output(led2, 0)
    time.sleep(1)

    GPIO.output(led3, 1)  # led verde 5s ligado
    time.sleep(5)
    GPIO.output(led3, 0)
    time.sleep(1)
