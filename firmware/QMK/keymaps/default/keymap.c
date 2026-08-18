// Copyright 2026
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

// hackpad has 3 switches wired directly (no diodes) to GP3, GP4, GP2 on a
// Seeed XIAO RP2040 (silkscreen labels D10, D9, D8). Top to bottom on the
// PCB: SW1, SW2, SW3. Swap any KC_* below to remap a key — see
// https://docs.qmk.fm/keycodes for the full list.
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        KC_VOLU,   // SW1 (top)    - volume up
        KC_MUTE,   // SW2 (middle) - mute
        KC_VOLD    // SW3 (bottom) - volume down
    ),
};
