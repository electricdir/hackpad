# hackpad

<img width="1920" height="890" alt="hackpad v4" src="https://github.com/user-attachments/assets/d6186e12-5f22-4aaf-a3c2-8f37bfd6491a" />
<img width="773" height="377" alt="image" src="https://github.com/user-attachments/assets/dc13ecfe-a637-4375-8ee8-66c3e4832413" />
<img width="349" height="846" alt="image" src="https://github.com/user-attachments/assets/dd81112b-bacd-41fd-9265-86ff869140ee" />

A 3-key macropad built around a Seeed XIAO RP2040.

## CAD Model

<img src=assets/cad.png alt="3D model of the case" width="500"/>

_(screenshot needed — drop a Fusion 360 render into `assets/cad.png`)_

3-piece 3D printed case (top, middle, bottom) — STLs in [`Production/`](Production).

## PCB

Schematic
<img src=assets/schematic.png alt="Schematic" width="600"/>

PCB
<img src=assets/pcb.png alt="pcb" width="300"/>

No diode matrix — each switch wires one leg to ground and the other
straight to a GPIO on the XIAO. Source: [`PCB/`](PCB).

## Firmware Overview

Runs on [KMK](https://github.com/KMKfw/kmk_firmware/) — pure Python on
CircuitPython, no compiler needed. See [`Firmware/main.py`](Firmware/main.py).

## BOM

- 1× Seeed XIAO RP2040 — main controller
- 3× Cherry MX-compatible mechanical switches
- 3× Cherry MX-compatible keycaps
- 1× Custom PCB
- 1× 3D printed case (top + middle + bottom) — printed from the STLs in [`Production/`](Production)
- M2 screws — for case assembly; qty/length depend on your case revision, check fit before ordering
- 1× USB-C cable — for flashing and everyday use

## License

MIT — see [LICENSE](LICENSE).
