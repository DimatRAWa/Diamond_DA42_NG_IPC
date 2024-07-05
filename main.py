import pandas as pd
import telebot
import settings

bot = telebot.TeleBot(settings.TOKEN)


def position_output():
    excel_file = settings.file
    sheet_number = 'Лист1'
    df = pd.read_excel(excel_file, sheet_name=sheet_number)
    df['P/N'] = df['P/N'].astype(str)
    return df

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Привет! Отправь P/N изделия.')

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    part_number = message.text.strip()
    position_df = position_output()
    position = position_df.loc[position_df['P/N'] == part_number, 'Position'].value
    bot.reply_to(message, f'Позиция {part_number}: {position}')


bot.polling(none_stop=True, interval=0)
