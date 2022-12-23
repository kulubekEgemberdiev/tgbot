import telebot
from telebot import types

bot = telebot.TeleBot('5612338105:AAF-BCpbVKHJxwn1-E8111cbiVN3eGdFy9Q')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}!")


@bot.message_handler(commands=['music'])
def music(message):
    music1 = open("muratti.mp3", "rb")
    bot.send_audio(message.chat.id, music1)


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, f"Ахаха, {message.from_user.first_name}, отличное фото!")


@bot.message_handler(commands=['openbtn'])
def tg_group(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти', url="https://t.me/pyproglib"))
    bot.send_message(message.chat.id, "Ссылка на группу 👇", reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton("/start")
    openbtn = types.KeyboardButton("/openbtn")
    id = types.KeyboardButton("id")
    markup.add(start, openbtn, id)
    bot.send_message(message.chat.id, "Кнопки 👇", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}!")
    elif message.text == "Hello":
        bot.send_message(message.chat.id, f"Hello, {message.from_user.full_name}!")
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ИД: {message.from_user.id}!")
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю!")


bot.polling(none_stop=True)
