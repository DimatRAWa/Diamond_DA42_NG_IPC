import pandas as pd
import telebot
import settings

bot = telebot.TeleBot(settings.TOKEN)

def load_orders():
    excel_file = settings.file
    sheet_name = 'Лист1'
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    df['P/N'] = df['P/N'].astype(str)
    return df

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Привет! Отправь P/N изделия.')

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    order_number = message.text.strip()
    orders_df = load_orders()
    position = orders_df.loc[orders_df['P/N'] == order_number, 'Position'].value
    bot.reply_to(message, f'Позиция {order_number}: {position}')


bot.polling(none_stop=True, interval=0)
