from selenium import webdriver
import RPi.GPIO as GPIO
import time
import board
from neopixel import NeoPixel

pixels = NeoPixel(board.D18, 30)

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=options)
driver.get('http://192.168.137.127')
        
while True:
    time.sleep(10)
    fire = driver.find_element_by_css_selector('body > span.fire > em').text
    gas = driver.find_element_by_css_selector('body > span.gas > em').text
    #print(fire)
    #print(gas)
    ifire = int(fire)
    igas = float(gas)
    if ifire == 0 and igas >= 300:
        buzzer_gpio = 23
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(buzzer, GPIO.OUT)
        GPIO.setwarnings(False)
        sound_list = [261, 294, 329, 349, 392, 440, 493 ,523]
        while True:
            try:
                p = GPIO.PWM(buzzer_gpio, 100) 
                p.start(100)
                p.ChangeDutyCycle(90)
                for i in range(8):
                    p.ChangeFrequency(sound_list[i])
                    time.sleep(1)
                p.stop()
                pixels.fill((255, 0, 0))
            except:pass
    else:pass


