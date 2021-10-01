# CircuitPython
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code

This code makes a LED slowly increase in color and slowly becomes more green.

```python
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)


dot.brightness = 0.1

r = 0
g = 0
b = 0
while True:

    if b < 240:
        b += 4
    if b == 240:
        g += 4
        b = 0
    if g == 240:
        r += 4
        g = 0
        b = 0
    
    dot.fill((r, g, b))
    time.sleep(0.01)
    print(r, g, b)
```


### Evidence
Pictures / Gifs of your work should go here.  You need to communicate what your thing does.
<img src="WIN-20210917-15-13-41-Pro.gif" alt="light">
### Wiring
The only requirement is a board.
### Reflection
The largest difficulty was learning python syntax and how to make it work correctly. I had to makke sure it was a += and a -= until I made it choose randomly




## CircuitPython_Servo

### Description & Code
this code uses capacitive touch to make the servo rotate
```python
import time
import board
import touchio
import servo
import pwmio
pwm = pwmio.PWMOut(board.A4, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)
touch_A1 = touchio.TouchIn(board.A1)  
touch_A2 = touchio.TouchIn(board.A0)  
A = 1
while True:
    if touch_A2.value and A < 180:
        A += 1
        print("hi")
    if touch_A1.value and A > 0:
        A -= 1
        print("there")
    my_servo.angle = A
    time.sleep(0.005)
    


```

### Evidence
<img src="WIN_20210915_15_19_20_Pro.gif" alt="servopic">
### Wiring

<img src="Servo.PNG" alt="servo">

### Reflection

Limits are a very good idea when you have a shifting number. forgetting them cost me a decent bit of time and was also stressful.



## CircuitPython_sensor

### Description & Code
this code makes a LED change color based on the distance to an object
```python

import time
import board
import adafruit_hcsr04
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
r = 0
g = 0
b = 0

while True:
    try:
        print(sonar.distance)
        if sonar.distance <= 15:
            r =  abs(round(sonar.distance-5 / 15*255))
        if sonar.distance >= 10 and sonar.distance <= 30:
            b = abs(round(sonar.distance-5 / 15*255))
        if sonar.distance >= 25:
            g = abs(round(sonar.distance-5 / 15*255))
        if sonar.distance > 25:
            r = 0
        if sonar.distance < 10 or sonar.distance > 30:
            b = 0
        if sonar.distance < 30:
            g = 0
        print(r, g, b)
    except RuntimeError:
        g = 255
        print("retrying")
    dot.fill((r, g, b))
    time.sleep(0.3)
	


```

### Evidence
<img src="https://github.com/Ashanks70/Circuitpython/blob/main/WIN_20210922_15_36_08_Pro.gif" alt="sensor">
### Wiring
<img src="ultrasonic.PNG" alt="sensor">
### Reflection
this one was very hard I had to make sure to round the number and take the absolute value to make sure the light did not bug out.




## photointerrupter

### Description & Code
this make the metro track the number of times that a photointerrupter has triggered.
```python
import board
import time
from digitalio import DigitalInOut, Direction, Pull

interrupter = DigitalInOut(board.D10)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP
start = time.time()
t = 0
c = 0
p = 0
second = 1
passed = 4
total = 0
scount = 0
counter = 0
while True:
    if time.monotonic() > total + passed:
        total += 4
        print("triggered:",counter,"times this rotation.")
        counter = 0
    elif interrupter.value == True and time.monotonic() > scount + second:
        counter += 1
        scount += 1


```

### Evidence
<img src="photointerrupter.gif" alt="servopic">
### Wiring
<img src="photointerrupter.PNG" alt="photointerupterw">
### Reflection
I learned how to use time monotonic and I also learned how much of a pain it can end up being. make sure that your new base is set to time monotonic.
