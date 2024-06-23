import pandas as pd
#import telebot
#import settings

#bot = telebot.TeleBot(settings.TOKEN)

excel_file = pd.read_excel('My_IPC.xlsx')
df = pd.DataFrame(excel_file, columns = ['P/N', 'ATA&Pos'])
print(df)

#def load_orders():
    #excel_file = 'My_IPC.xlsx'  # Путь к файлу Excel
    #sheet_name = 'Лист1'  # Имя листа с P/N
    #df = pd.read_excel(excel_file, sheet_name=sheet_name)  # Загрузка данных в DataFrame
    #df['P/N'] = df['P/N'].astype(str)
    #print(df)
    #return df
#print(load_orders, 'successfully executed')

#@bot.message_handler(commands=['start'])
#def handle_start(message):
    #bot.reply_to(message, 'Привет. Напиши P/N.')
#print(handle_start, 'successfully executed')

#@bot.message_handler(func=lambda message: True)
#def hadler_text(message):
    #order_number = message.text.strip()
    #orders_df = load_orders()  # Загрузка данных из Excel-таблицы
    #status = orders_df.loc[orders_df['P/N'] == order_number, 'ATA&Pos'].values  # Поиск позиции
    #bot.reply_to(message, f'P/N {order_number}: {status[0]}')
#print(hadler_text, 'successfully executed')

#bot.polling()