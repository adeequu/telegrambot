import re 
import pyowm
from datetime import timedelta, datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    CallbackContext,
    Updater, 
    CommandHandler, 
    PicklePersistence, 
    Filters, 
    MessageHandler,
    CallbackQueryHandler
)
from telegram.ext.messagehandler import MessageHandler
from telegram.message import Message
from menu import regions_keyboard, raion_keyboard
from credentials import TOKEN
from key_button import regions_buttons, raion_menu
from message import arena, abdushata, lcentr, chelsea, madrid45, alamedin, footbolistan, alai, pyatnol, akshumkar, darbaza, arsenal, text2

def start(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEDUCVhlhdyRjbayCY84g88TmpddswTGgAC-wIAAnFRiQb_ElF88IFkPCIE'
    ) 
    update.message.reply_text(
        "Добро пожаловать, {username}, Это FreestyleBot. Бот котрый поможет тебе найти поля в твоем городе. Выберите город: ".format(
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                else update.effective_user.username),
        reply_markup=regions_keyboard()
    )

def get_weather():
    degree = '\N{DEGREE SIGN}'
    weather_5 = ''
    owm = pyowm.OWM('b03d46f730e8aa549ef16b42b951d701')
    forecast = owm.three_hours_forecast('Bishkek, KG')
    for i in range(5):
        time = datetime.now() + timedelta(days=i)
        weather = forecast.get_weather_at(time)
        temperature = weather.get_temperature(unit='celsius')['temp']
        weather_5 =weather_5 + f"{time.strftime('%Y-%m-%d')} {temperature} °C \n"
        # print(time.strftime('%Y-%m-%d')+' '+ str(temperature) +' C')
    return weather_5


REGION_REGEX = r"(?=(" + (regions_buttons[0]) + r"))"
RAION_REGEX = r"(?=(" + (raion_menu[0]) + r"))"
RAION1_REGEX = r"(?=(" + (raion_menu[1]) + r"))"
RAION2_REGEX = r"(?=(" + (raion_menu[2]) + r"))"
RAION3_REGEX = r"(?=(" + (raion_menu[3]) + r"))"
RAION4_REGEX = r"(?=(" + (raion_menu[4]) + r"))"




def zapisat(update: Update, context:CallbackContext):
    z = update.message.text
    print(z[:6])
    if z[:6] == 'Запись':
        context.bot.send_message(
            chat_id = '@footbollpolya', 
            text = z
        )


def zapis(update: Update, context: CallbackContext):
    info=re.match(RAION4_REGEX, update.message.text)
    update.message.reply_text(
        text2
    )       


def oktabr_inline_buttons():
    keyboard = [
        [InlineKeyboardButton("Арена⚽️", callback_data='арена⚽️')],
        [InlineKeyboardButton("Абдышата⚽️", callback_data='абдышата⚽️')],
        [InlineKeyboardButton("Лцентр⚽️", callback_data='лцентр⚽️')],
        [InlineKeyboardButton("Погода☁️", callback_data='погода☁️')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def sverlov_inline_buttons():
    keyboard1 = [
        [InlineKeyboardButton("Челси⚽️", callback_data='челси⚽️')],
        [InlineKeyboardButton("Мадрид45⚽️", callback_data='мадрид45⚽️')],
        [InlineKeyboardButton("Аламедин⚽️", callback_data='аламедин⚽️')],
        [InlineKeyboardButton("Погода☁️", callback_data='погода☁️')],
        
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard1)
    return reply_markup1

def pervomai_inline_buttons():
    keyboard2 = [
        [InlineKeyboardButton("Футболистан⚽️", callback_data='футболистан⚽️')],
        [InlineKeyboardButton("Алай⚽️", callback_data='алай⚽️')],
        [InlineKeyboardButton("Пятьноль⚽️", callback_data='пятьноль⚽️')],
        [InlineKeyboardButton("Погода☁️", callback_data='погода☁️')],
        
    ]
    reply_markup2 = InlineKeyboardMarkup(keyboard2)
    return reply_markup2

def lenin_inline_buttons():
    keyboard3 = [
        [InlineKeyboardButton("Акшумкар⚽️", callback_data='акшумкар⚽️')],
        [InlineKeyboardButton("Дарбаза⚽️", callback_data='дарбаза⚽️')],
        [InlineKeyboardButton("Арсенал⚽️", callback_data='арсенал⚽️')],
        [InlineKeyboardButton("Погода☁️", callback_data='погода☁️')],

    ]
    reply_markup3 = InlineKeyboardMarkup(keyboard3)
    return reply_markup3


def recive_course_menu(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEDUClhlhgzmEovyL9DDJ0iqk8Nj4QVQQACNQADr8ZRGntbZmxEzh82IgQ'
    ) 
    info = re.match(REGION_REGEX, update.message.text)
    update.message.reply_text(
        "Выберите район",
        reply_markup=raion_keyboard()
    )


def recive_october_menu(update: Update, context: CallbackContext): 
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEDUCNhlhbhL_iI4pS77FPrQzegxkLh_gAC1AIAAnFRiQa3r1kaY91mvCIE'
    )   
    info = re.match(RAION_REGEX, update.message.text)
    update.message.reply_text(
        'Выберите поле',
        reply_markup=oktabr_inline_buttons()
    
    )

def recive_sverlov_menu(update: Update, context: CallbackContext):
    info = re.match(RAION1_REGEX, update.message.text)
    update.message.reply_text(
        'Выберите поле',
        reply_markup=sverlov_inline_buttons()
    
    )

def recive_pervomai_menu(update: Update, context: CallbackContext):
    info = re.match(RAION2_REGEX, update.message.text)
    update.message.reply_text(
        'Выберите поле',
        reply_markup=pervomai_inline_buttons()

    )

def recive_lenin_menu(update: Update, context: CallbackContext):
    info = re.match(RAION3_REGEX, update.message.text)
    update.message.reply_text(
        'Выберите поле',
        reply_markup=lenin_inline_buttons()

    )


def inline_buttons(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Арена⚽️", callback_data='арена⚽️')],
        [InlineKeyboardButton("Абдышата⚽️", callback_data='абдышата⚽️')],
        [InlineKeyboardButton("Лцентр⚽️", callback_data='лцентр⚽️')],
        [InlineKeyboardButton("Погода☁️", callback_data='погода☁️')],
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    query.answer()
    keyboard1 = [
        [InlineKeyboardButton("Челси⚽️", callback_data='челси⚽️')],
        [InlineKeyboardButton("Мадрид45⚽️", callback_data='мадрид45⚽️')],
        [InlineKeyboardButton("Аламедин⚽️", callback_data='аламедин⚽️')],
        [InlineKeyboardButton("Погода☁️", callback_data='погода☁️')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard1)
    query = update.callback_query
    query.answer()
    keyboard2 = [
        [InlineKeyboardButton("Футболистан⚽️", callback_data='футболистан⚽️')],
        [InlineKeyboardButton("Алай⚽️", callback_data='алай⚽️')],
        [InlineKeyboardButton("Пятьноль⚽️", callback_data='пятьноль⚽️')],
        [InlineKeyboardButton("Погода☁️", callback_data='погода☁️')],
    ]
    reply_markup2 = InlineKeyboardMarkup(keyboard2)
    query = update.callback_query
    query.answer()
    keyboard3 = [
        [InlineKeyboardButton("Акшумкар⚽️", callback_data='акшумкар⚽️')],
        [InlineKeyboardButton("Дарбаза⚽️", callback_data='дарбаза⚽️')],
        [InlineKeyboardButton("Арсенал⚽️", callback_data='арсенал⚽️')],
        [InlineKeyboardButton("Погода☁️", callback_data='погода☁️')],
    ]
    reply_markup3 = InlineKeyboardMarkup(keyboard3)
    query = update.callback_query
    query.answer()
    # ----
    if query.data == 'арена⚽️':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text = arena

        )

        query.message.reply_photo(
            open('photo/arena2.jpg','rb'),
            
        )
        query.message.reply_location(
            longitude=74.6329110068158,
            latitude=42.82236510658675,
            reply_markup=oktabr_inline_buttons()
        )

    if query.data == 'абдышата⚽️':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=abdushata
        )

        query.message.reply_photo(
            open('photo/abdushata.jpg','rb'),

        )
        query.message.reply_location(
            longitude=74.6270764515818,
            latitude=42.823140008556486,
            reply_markup=oktabr_inline_buttons()
        )

    if query.data == 'лцентр⚽️':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=lcentr

        )    

        query.message.reply_photo(
            open('photo/lcentr.jpg','rb'), 
        
        )
        query.message.reply_location(
            longitude=74.61865238415265,
            latitude=42.83866705276821,
            reply_markup=oktabr_inline_buttons() 
            
        )
        # -----
        
    if query.data == 'челси⚽️':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text = chelsea

        )

        query.message.reply_photo(
            open('photo/chelsea.jpg','rb'), 

        )
        query.message.reply_location(
            longitude=42.87175307646615,
            latitude=42.87175307646615,
            reply_markup=sverlov_inline_buttons()

        )

    if query.data == 'мадрид45⚽️':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=madrid45

        )

        query.message.reply_photo(
            open('photo/madrid45.jpg','rb'), 
            
        )

        query.message.reply_location(
            longitude=74.63566099367003,
            latitude=42.8827494547276,
            reply_markup=sverlov_inline_buttons()    

        )
    if query.data == 'аламедин⚽️':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=alamedin

        )

        query.message.reply_photo(
            open('photo/alamedin.jpg','rb'),
        
        )
        
        query.message.reply_location(
            longitude=74.68411843276073,
            latitude=42.87766115350216,
            reply_markup=sverlov_inline_buttons()
             
        )
        # ------
    if query.data == 'футболистан⚽️':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=footbolistan

        )

        query.message.reply_photo(
            open('photo/footbolistan.jpg','rb'),
        
        )
        
        query.message.reply_location(
            longitude=74.60745873599211,
            latitude=42.85602023068493,
            reply_markup=pervomai_inline_buttons()

        )

    if query.data == 'алай⚽️':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=alai

        )

        query.message.reply_photo(
            open('photo/alai.jpg','rb'),
            
        )
        
        query.message.reply_location(
            longitude=74.53917554848663,
            latitude=42.87675551261356,
            reply_markup=pervomai_inline_buttons()    

        )
    
    if query.data == 'пятьноль⚽️':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=pyatnol

        )

        query.message.reply_photo(
            open('photo/pyatnol.jpg','rb'),
        
        )
        
        query.message.reply_location(
            longitude=74.59635223199959,
            latitude=42.84692692971213,
            reply_markup=pervomai_inline_buttons()

        )
        # --------
    if query.data == 'акшумкар⚽️':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=akshumkar

        )

        query.message.reply_photo(
            open('photo/akshumkar.jpg','rb'),            
            
        )
        
        query.message.reply_location(
            longitude=74.58526430628147,
            latitude=42.848120761224266,
            reply_markup=lenin_inline_buttons()

        )

    if query.data == 'дарбаза⚽️':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=darbaza

        )

        query.message.reply_photo(
            open('photo/darbaza.jpg','rb'), 
        )
        
        query.message.reply_location(
            longitude=74.5352787801669,
            latitude=42.851991181181965,
            reply_markup=lenin_inline_buttons()
        

        )
    
    if query.data == 'арсенал⚽️':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=arsenal

        )

        query.message.reply_photo(
            open('photo/arsenal.jpg','rb'),    
        )
        
        query.message.reply_location(
            longitude=74.56234198201115,
            latitude=42.834290301150055,
            reply_markup=lenin_inline_buttons()

        )
    if query.data == 'погода☁️':

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=get_weather()

        )
    






updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data')) 


updater.dispatcher.add_handler(CommandHandler('start', start))


updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(REGION_REGEX),
    recive_course_menu
    ))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(RAION_REGEX),
    recive_october_menu
    ))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(RAION1_REGEX),
    recive_sverlov_menu
    ))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(RAION2_REGEX),
    recive_pervomai_menu
    ))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(RAION3_REGEX),
    recive_lenin_menu
    ))
    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(RAION4_REGEX),
    zapis
    ))

updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    zapisat
    ))


updater.dispatcher.add_handler(CallbackQueryHandler(inline_buttons))



updater.start_polling()
updater.idle()