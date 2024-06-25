import pandas as pd
import telebot
import settings

bot = telebot.TeleBot(settings.TOKEN)

excel_file = pd.read_excel(settings.file)
df = pd.DataFrame(excel_file, columns = ['P/N', 'ATA&Pos'])
print(df)

@bot.message_handler(commands = ['start'])
def start(m, res = False):
    bot.send_message(m.chat.id, 'Отправьте P/N')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == 'A508-28' or message.text == 'a508-28':
        bot.send_message(message.chat.id, '33-40-03-1_Pos.120')
    elif message.text == '02-0250276-00':
        bot.send_message(message.chat.id, '33-40-03-1_Pos.100')
    elif message.text == '01-0770062-05':
        bot.send_message(message.chat.id, '33-40-03-1_Pos.200')
    elif message.text == 'W1290-28':
        bot.send_message(message.chat.id, '33-40-03-1_Pos.110')
    elif message.text == 'BW1-B12-RY8-RY6-150':
        bot.send_message(message.chat.id, '32-10-02-1_Pos.690')
    elif message.text == 'BW1-B14-RB6-RB6-200':
        bot.send_message(message.chat.id, '32-20-01-1_Pos.650')
    elif message.text == '/help':
        bot.send_message(message.chat.id, 'Напиши P/N')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю, напиши /help.')

bot.polling(none_stop = True, interval = 0)
