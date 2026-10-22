import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

# Each switch: XIAO RP2040 pin -> switch -> GND
PINS = [
    board.D8,    # key 1 - Copy
    board.D9,    # key 2 - Paste
    board.D10,   # key 3 - Print Screen
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  # switch connects pin to GND
    pull=True,                 # internal pull-up resistor
    interval=0.01,
    debounce_threshold=5,
)

keyboard.keymap = [
    [
        KC.LCTL(KC.C),   # 1. Copy (Ctrl+C)
        KC.LCTL(KC.V),   # 2. Paste (Ctrl+V)
        KC.PSCR,         # 3. Print Screen
    ],
]

if __name__ == '__main__':
    keyboard.go()
