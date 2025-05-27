import time
import array
import math
import board
import neopixel
import analogio

pixel_pin = board.D2
num_pixels = 16

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.7, auto_write=False)

mic_pin = board.A2
mic = analogio.AnalogIn(mic_pin)

previous_mic_value = 0

color_value = mic.value/455
mic_value_array = array.array('i', [0, 0])

while True:
    mic_value = abs(mic.value)
    
    print("difference:")
    print(previous_mic_value - int(mic_value/455) < 50)
    print(previous_mic_value - int(mic_value/455))
    
    if previous_mic_value - int(mic_value/455) < 50:
        print("hi")
        previous_mic_value = int(mic_value/455)
        color_value = int(mic_value/455)
        COLOR = (color_value, 0, 0)
        pixels.fill(COLOR)
        pixels.show()

    print((color_value,))
    
    # print(mic.value)
    # time.sleep(1)
    # print(mic_value_array)
