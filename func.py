import telebot
import pandas as pd
import settings

bot = telebot.TeleBot(settings.TOKEN)  # Создание бота c использованием ключа Telegrame.

def position_output():  # Создание функции обработки/загрузки данных в DataFrame.
    excel_file = settings.file  # Путь к файлу Excel.
    sheet_number = 'Лист1'  # Имя листа с P/N.
    df = pd.read_excel(excel_file, sheet_name=sheet_number)  # Загрузка данных в DataFrame.
    df['P/N'] = df['P/N'].astype(str)  # Преобразование методом .astype(str) столбцо с данными в сткроки
    return df

@bot.message_handler(commands=['start'])  # Декоратор, реагирующий на команду /start.
def handle_start(message):  # Создание функции привественного сообщения.
    bot.reply_to(message, 'Привет! Отправь P/N изделия!')  # Приветственное сообщение!

@bot.message_handler(func=lambda message: True)
def handle_text(message):  # Обработчик входящих сообщений от пользователя.
    part_number = message.text.strip()
    position_df = position_output()
    position = position_df.loc[position_df['P/N'] == part_number, 'Position'].values  # Выбор из фрейма данных
    bot.reply_to(message, f'{position[0]}')
