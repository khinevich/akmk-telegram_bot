import telebot
from telebot import types as tp

bot = telebot.TeleBot('5359668177:AAGriKhPw7fmS3PhLpBPPRMColzpUAbj9Zc')

@bot.message_handler(commands=['start'])
def start(message):
    mess_1=f'Hello,<b>{message.from_user.first_name}</b> aka <b><u>{message.from_user.username}</u></b>, welcome to our test bot version.'
    bot.send_message(message.chat.id, mess_1, parse_mode='html')
    bot.send_message(message.chat.id,'<b>I hope, you will enjoy it!</b>', parse_mode='html')

'''@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "me too":
        bot.send_message(message.chat.id, "Great to hear it! What do you want to recieve from me?", parse_mode='html')
    
    elif message.text=='photo' or message.text=='фото':
        bot.send_message(message.chat.id, "which one? <b>Andrii</b>, <b>Anton</b> or <b>Mikhail</b>?", parse_mode='html')
    elif message.text=='Andrii':
        photo=open('photo/Andrii.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text=='Mikhail':
        photo=open('photo/Mikhail.JPG', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text=='Anton':
        photo=open('photo/Anton.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "I dont understand you.", parse_mode='html')'''

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Wow such a cool photo')

@bot.message_handler(commands=['website'])
def website(message):
    markup = tp.InlineKeyboardMarkup()  #встроенный в сообщения кнопки
    markup.add(tp.InlineKeyboardButton('Open this link:', url='https://www.linkedin.com/in/mikhail-khinevich-a56399219/'))
    bot.send_message(message.chat.id, 'Go to the website', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    markup = tp.ReplyKeyboardMarkup(resize_keyboard=True)              
    instagram = tp.KeyboardButton('Instagram')
    linkdin = tp.KeyboardButton('LinkdIN')
    markup.add(instagram, linkdin)
    bot.send_message(message.chat.id, 'Go to the website', reply_markup=markup)

bot.polling(none_stop=True) 
