#  Twistpad
My submission for the Hack Club Hackpad project.


This repository contains all the files needed to produce a Twistpad, created by me. The Twistpad consists of a 3x3 grid of standard keys, which are bound to F13 - F21. On the right side of the grid, there are two dials, and the top one is bound to volume while the bottom one is bound to video controls (forward, backward, etc.). Additionally, there are LEDs, because who doesn't like a little RGB? I created this project over the course of nearly two weeks, using KiCad for the PCB, Fusion360 for the case design, and VSCode and Python for the firmware. 

So without further adieu, I present... the Twistpad!

## The hackpad:
A wonderful side view to give you an idea of the height

<img width="1420" height="905" alt="image" src="https://github.com/user-attachments/assets/9cda27bc-45e5-4635-9534-dcd553624bdb" />

And then a top view so you can look through the window in the top right! (that tiny thing took me quite a long time)

<img width="1181" height="978" alt="image" src="https://github.com/user-attachments/assets/fd0141f5-c1a6-4cbd-b35b-ba443d455e9f" />

The hackpad consists of a simple case design, with filleted corners and cutouts in the top to provide psace for the keys and dials to poke through. I wanted to add some extra stuff, so I spend time on the USB cutout (pictured below) making it look good and having it have a little inwards slant. i also spend time making the window into the PCB, which displays the Seeeduino logo perfectly. 

<img width="1273" height="525" alt="Screenshot 2026-06-24 124018" src="https://github.com/user-attachments/assets/55a09565-980e-44dc-83c8-3f1cacf9530e" />


## Schematic of the PCB:
Made on KiCad, it was quite fun and easy to make it, no need to worry about physical space and stuff. 

<img width="1811" height="898" alt="image" src="https://github.com/user-attachments/assets/27745e4b-a557-4343-8786-5405c98e5a1a" />

The glorious PCB itself:
Also made on KiCad, it was also fun to do this, once I learned about vias. Has thicker traces for the 5V lines. 

<img width="966" height="770" alt="image" src="https://github.com/user-attachments/assets/48da54bc-6bdf-4744-9f71-9932d7cb97fb" />

## The case itself
This image pictures both the top plate and bottom part of the case, seperated. They fit together using M3x16mm screws along with M3x5mx4mm heatset inserts through the 4 holes on each corner of the case. In total, there are only 2 printed parts, the top and the bottom.

<img width="1343" height="835" alt="image" src="https://github.com/user-attachments/assets/2652f50e-755f-40b5-8576-8bf736b6f431" />

## The Firmware
This hackpad uses KMK firmware, and it was coded on VSCode using Python. 

## The BOM
1x Seeed XIAO RP2040

11x through-hold 1N4148 Diodes

9x MX-Style Switches

2x EC11 Rotary Encoders

9x white (or really any color or design you want) DSA keycaps

9x SK6812 MINI-E LEDs

4x M3x16mm screws

4x M3x5mx4mm heatset inserts


## Controls and binds
Imagine a 3x3 grid

A B C

D E F

G H I

Key A is bound to F13

Key B is bound to F14

Key C is bound to F15

Key D is bound to F16

Key E is bound to F17

Key F is bound to F18

Key G is bound to F19

Key H is bound to F20

Key I is bound to F21

In addition to that, due to a lack of pins, clicking down on the top dial is also mapped to whatever Key C is mapped to, and clicking down on the bottom dial is mapped to whatever Key I is mapped to.
Turning the top dial controls the volume, and turning the bottom dial controls video progress, like going forward in the video or backwards.
