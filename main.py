#Бот

""" PETUCH_T_BOT """

import telebot
import constant
import os

bot = telebot.TeleBot(constant.token)

print(bot.get_me())

def log(message, answer):
    print("\n ~~~~~")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))
    print(answer)

@bot.message_handler(commands=["start"])
def handle_command(message):
    bot.send_message(message.chat.id, """ Ко-ко, меня зовут Петуч, если нужна будет моя помощь, то набери /help """)

@bot.message_handler(commands=["help"])
def handle_command(message):
    bot.send_message(message.chat.id, """ Пока я тебе ничем не могу помочь, sry (( """)

@bot.message_handler(commands=["action"])
def handle_command(message):
    bot.send_message(message.chat.id, """ Ко-ко! Хочешь горячих цыпочек? Конечно хочешь! """)
    directory = "D:\Program Files\python\petuch_t_bot\Photo"
    all_files_in_directory = os.listdir(directory)
    for file in all_files_in_directory:
        img = open(directory + '/' + file, 'rb')
        bot.send_photo(message.from_user.id, img)
        img.close()
    bot.send_message(message.chat.id, """Держи тебе горячих ципочек, бро. КО-КО""")
    log(message, "ПОЛЬЗОВАТЕЛЬ СМОТРИТ ЦЫПОЧЕК 18+ без СМС и регистрации!!! ШОК!")




@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = "Хочешь снесу яйцо? (да/нет)"
    if message.text == "да":
        answer = "Ты че дурашка? Я же петух!"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == "нет":
        answer = "Не очень то и хотелось"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == "ты лох":
        answer = "иди нахуй"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    else:
        bot.send_message(message.chat.id, answer )
        log(message, answer)

bot.polling(none_stop=True, interval=0)