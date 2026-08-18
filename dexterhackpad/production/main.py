import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

# hackpad has 3 switches wired directly (no diode matrix) - one leg to
# ground, the other straight to a GPIO. board.D10/D9/D8 match the XIAO
# RP2040's own silkscreen labels, so no GPIO-number translation needed.
# Top to bottom on the PCB: SW1, SW2, SW3.
keyboard.matrix = KeysScanner(
    pins=(board.D10, board.D9, board.D8),
    value_when_pressed=False,  # switches pull the pin to ground when pressed
)

# Swap any KC.* below to remap a key - see
# https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
keyboard.keymap = [
    [
        KC.VOLU,  # SW1 (top)    - volume up
        KC.MUTE,  # SW2 (middle) - mute
        KC.VOLD,  # SW3 (bottom) - volume down
    ],
]

if __name__ == '__main__':
    keyboard.go()
