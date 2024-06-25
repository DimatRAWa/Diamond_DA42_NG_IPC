import telebot
import settings

bot = telebot.TeleBot(settings.TOKEN)

@bot.message_handler(commands = ['start'])
def start(m, res = False):
    bot.send_message(m.chat.id, 'Отправьте P/N')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == 'A508-28' or message.text == 'a508-28':
        bot.send_message(message.chat.id, '33-40-03-1_Pos.120')
    elif message.text == 'W1290-28':
        bot.send_message(message.chat.id, '33-40-03-1_Pos.110')
    elif message.text == '/help':
        bot.send_message(message.chat.id, 'Напиши P/N')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю, напиши /help.')

bot.polling(none_stop = True, interval = 0)
