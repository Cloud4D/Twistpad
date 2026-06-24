import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB

# keyboard brain
keyboard = KMKKeyboard()

# mapping the rows and columns and pins
keyboard.row_pins = (board.D0, board.D1, board.D2)
keyboard.col_pins = (board.D7, board.D8, board.D9,)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# intializing the rotary dial handlers
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.divisor = 4  # changes sensitivity

# configuring the rotary dial pins
encoder_handler.pins = (
    (board.D6, board.D5, None, False),
    (board.D4, board.D3, None, False),
)

# rgb
rgb = RGB(pixel_pin=board.D10, num_pixels=9)
keyboard.extensions.append(rgb)

# defining the keys
keyboard.keymap = [
    [
        KC.F13, KC.F14, KC.F15, # sw1, sw4, sw9, 
        KC.F16, KC.F17, KC.F18, # sw2, sw5, sw10, 
        KC.F19, KC.F20, KC.F21, # sw3, sw6, sw11, 
    ]
]

# defining the dials
encoder_handler.map = [
    (
        (KC.VOLD, KC.VOLU),
        (KC.LEFT, KC.RGHT)
    )
]

#startup loop
if __name__ == "__main__":
    keyboard.go()