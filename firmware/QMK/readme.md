# hackpad (QMK)

* Keyboard Maintainer: [aavin](https://github.com/aavin)
* Hardware Supported: Seeed XIAO RP2040

No diode matrix — each switch wires one leg to ground and the other
straight to its own GPIO, so this uses QMK's `direct` pin matrix (1x3).

| Switch | XIAO pin | RP2040 GPIO |
|--------|----------|-------------|
| SW1 (top)    | D10 | GP3 |
| SW2 (middle) | D9  | GP4 |
| SW3 (bottom) | D8  | GP2 |

## Build

Drop this folder into `qmk_firmware/keyboards/hackpad`, then:

```bash
qmk compile -kb hackpad -km default
```

## Flash

Put the board in bootloader mode (hold BOOT while plugging in USB, or
double-tap RESET), then:

```bash
qmk flash -kb hackpad -km default
```

or drag the built `.uf2` (in `qmk_firmware/.build/`) onto the `RPI-RP2`
drive.

## Remap keys

Edit `keymaps/default/keymap.c`. Keycode reference: https://docs.qmk.fm/keycodes
