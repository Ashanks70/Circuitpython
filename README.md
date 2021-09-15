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

This code makes a LED blink at random intervals with random colors.

Here's how you make code look like code:
```python
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

```


### Evidence
Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring
The only requirement is a board.
### Reflection
The largest difficulty was learning python syntax and how to make it work correctly. I had to makke sure it was a += and a -= until I made it choose randomly




## CircuitPython_Servo

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection




## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
