import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)


dot.brightness = 0.1

r = 0
g = 0
b = 0
while True:

    if b < 160:
        b + 4
    if b == 160:
        g = 4
        b = 0
    dot.fill((r, g, b))
print(r, g, b)
