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

color_value = mic.value/455
mic_value_array = array.array('i', [0, 0])

def calculate_mean(data_array):
  if not data_array:
    return 0
  total = sum(data_array)
  mean = total / len(data_array)
  return mean

while True:
    if mic.value < 65025:
        mic_value_array.append(int(mic.value/455))

        COLOR = (int(mic.value/455), 0, 0)
        color_value = int(mic.value/455)
        pixels.fill(COLOR)
        pixels.show()

    #print((color_value,))
    #print(mic_value_array)
