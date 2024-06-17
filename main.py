import telebot
import settings
import pandas as pd

bot = telebot.TeleBot(settings.TOKEN)

# def load_order():
    # excel_file = 'My_IPC.xlsx' # Путь к файлу Excel
    # sheet_name = 'Лист1' # Имя листа с P/N
    # df = pd.read_excel(excel_file, sheet_name)

@bot.message_handler(content_types = ["text"])
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