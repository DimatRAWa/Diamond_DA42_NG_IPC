import telebot
import pandas as pd
import settings
from telebot import types

bot = telebot.TeleBot(settings.TOKEN)  # Создание бота c использованием ключа Telegrame.


def position_output():  # Создание функции обработки/загрузки данных в DataFrame.
    excel_file = settings.file  # Путь к файлу Excel.
    sheet_number = 'Лист1'  # Имя листа с P/N.
    df = pd.read_excel(excel_file, sheet_name=sheet_number)  # Загрузка данных в DataFrame.
    df['P/N'] = df['P/N'].astype(str)  # Преобразование методом .astype(str) столбцов с данными в сткроки.
    return df

def start_message(bot):
    @bot.message_handler(commands=['start'])  # Декоратор, реагирующий на команду /start.
    def handle_start(message):  # Создание функции приветственного сообщения.
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton('Diamond', url='https://www.diamondaircraft.com/en/')
        keyboard.add(button)
        bot.send_message(message.chat.id, 'Привет! Отправь P/N изделия!'.format(message.from_user), reply_markup=keyboard)

def text_message(bot):
    @bot.message_handler(func=lambda message: True)
    def handle_text(message):  # Обработчик входящих сообщений от пользователя.
        part_number = message.text.strip()
        position_df = position_output()
        position = position_df.loc[position_df['P/N'] == part_number, 'Position'].values  # Выбор из фрейма данных.
        bot.reply_to(message, f'{position[0]}')
