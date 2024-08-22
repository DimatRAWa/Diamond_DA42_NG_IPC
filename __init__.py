import telebot  # Добавляем библиотеку telebot для создания Телеграмм-бота.
import settings  # Импортируем файл с данными.
import func  # Импортиеруем функции.

bot = telebot.TeleBot(settings.TOKEN)  # Создание бота c использованием ключа Telegram.

func.position_output()  # Вызов функции обработки/загрузки данных в DataFrame.

func.start_message(bot)  # Вызов функции приветственного сообщения.

func.text_message(bot)  # Вызов функции входящих сообщений от пользователя.

bot.polling(none_stop=True, interval=0)  # Функция опроса сервера Telegram на предмет новых сообщений.
