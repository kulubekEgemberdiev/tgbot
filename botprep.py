import telebot
from telebot import types

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Hello, {message.from_user.full_name}!"
    bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['photo'])
def photo(message):
    photo = open("Telegram-logo.png", "rb")
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, f"Wow, {message.from_user.first_name}, great photo 👍🏾!")


@bot.message_handler(content_types=['sticker'])
def get_user_photo(message):
    bot.send_message(message.chat.id, f"Wow, {message.from_user.first_name}, nice sticker 👍🏾!")


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton("/start")
    group = types.KeyboardButton("/group")
    id = types.KeyboardButton("id")
    markup.add(start, group, id)
    bot.send_message(message.chat.id, "Кнопки 👇", reply_markup=markup)


@bot.message_handler(commands=['group'])
def tg_group(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Переход", url="https://t.me/"))
    bot.send_message(message.chat.id, "Ссылка на группу 👇🏾", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, f"Hello, {message.from_user.full_name}!")
    elif message.text == "Привет":
        bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}!")
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Your id: {message.from_user.id}!")
    else:
        bot.send_message(message.chat.id, "Я не понимаю тебя :( ")


bot.polling(none_stop=True)
