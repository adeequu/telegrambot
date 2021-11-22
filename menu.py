import telegram
from key_button import regions_buttons, raion_menu, oktober_menu




def regions_keyboard():
    keyboard=([
        [
            telegram.KeyboardButton(regions_buttons[0]),
            
        ]

    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )

def raion_keyboard():
    keyboard=([
        [
            telegram.KeyboardButton(raion_menu[0]),
            
        ],
        [
           telegram.KeyboardButton(raion_menu[1])
        ], 
        
        [
           telegram.KeyboardButton(raion_menu[2])

        ],

        [

        
           telegram.KeyboardButton(raion_menu[3])
        ],

        [
        
           telegram.KeyboardButton(raion_menu[4])

        ]
        ]
 
    )
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False


    )

def oktober_keyboard():
    keyboard=([
        [
            telegram.KeyboardButton(oktober_menu[0]),
            telegram.KeyboardButton(oktober_menu[1])
        ],
        [
          telegram.KeyboardButton(oktober_menu[2]),
          telegram.KeyboardButton(oktober_menu[3]),
          
        ]

    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )