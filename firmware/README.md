# Firmware

Two firmware options for the same hardware — pick one.

## [KMK](KMK/) — recommended

Pure Python, running on CircuitPython. No compiler, no build step — just
copy files onto the board. See [KMK/main.py](KMK/main.py).

## [QMK](QMK/)

The more traditional C-based keyboard firmware. Needs the QMK build
toolchain to compile. See [QMK/readme.md](QMK/readme.md) for build/flash
steps.

## Hardware

No diode matrix — each of the 3 switches wires one leg to ground and the
other straight to a GPIO on the Seeed XIAO RP2040.

| Switch | XIAO pin |
|--------|----------|
| SW1 (top)    | D10 |
| SW2 (middle) | D9  |
| SW3 (bottom) | D8  |
