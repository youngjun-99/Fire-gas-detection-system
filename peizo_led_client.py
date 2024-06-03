import time
import board
import requests
import RPi.GPIO as GPIO
from neopixel import NeoPixel

# PREFIX
SERVER_IP = "192.168.137.127"
BUZZER_GPIO = 23
PIXEL_PIN = board.D18
NUM_PIXELS = 30
URL = f"http://{SERVER_IP}/api/data"
SOUND_VALUES = [261, 294, 329, 349, 392, 440, 493, 523]  # 도레미파솔라시도
CHECK_INTERVAL = 10

# Initialize NeoPixel and GPIO
pixels = NeoPixel(PIXEL_PIN, NUM_PIXELS)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_GPIO, GPIO.OUT)
GPIO.setwarnings(False)

def fetch_sensor_data(url: str):
    """
    지정된 URL에서 센서 데이터를 가져오는 기능.

    Parameters:
        url (str): 데이터를 가져올 URL.

    Returns:
        dict: 요청이 성공한 경우 센서데이터가 포함된 dictionary.
        None: 요청 중 오류가 발생한 경우.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

def sound_alarm(buzzer_gpio: int, sound_values: list[int]):
    """
    부저를 사용하여 알람을 울리고 NeoPixel 스트립 색을 변경하는 기능.

    Parameters:
        buzzer_gpio (int): 부저가 연결된 GPIO 핀 번호.
        sound_values (list[int]): 부저를 통해 재생할 주파수 목록.

    Returns:
        None
    """
    try:
        p = GPIO.PWM(buzzer_gpio, 100)
        p.start(100)
        p.ChangeDutyCycle(90)
        for frequency in sound_values:
            p.ChangeFrequency(frequency)
            time.sleep(1)
        p.stop()
        pixels.fill((255, 0, 0))  # Red color for alarm
    except Exception as e:
        print("An unexpected error occurred while alarm:", e)

def main():
    """
    반복적으로 센서 데이터를 가져와서 조건이 충족되면 알람을 발생시키는 주요 기능.

    Returns:
        None
    """
    while True:
        sensor_data = fetch_sensor_data(URL)
        if sensor_data:
            if sensor_data['fire'] == 0 and sensor_data['gas'] >= 300:
                sound_alarm(BUZZER_GPIO, SOUND_VALUES)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        GPIO.cleanup()
        pixels.fill((0, 0, 0))  # Turn off NeoPixels
