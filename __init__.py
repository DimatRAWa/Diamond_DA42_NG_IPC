import telebot  # Добавляем библиотеку telebot для создания Телеграмм-бота.
import settings  # Импортируем файл с данными.
import func  # Импортиеруем функции.

bot = telebot.TeleBot(settings.TOKEN)  # Создание бота c использованием ключа Telegrame.

func.position_output()  # Импорт функции обработки/загрузки данных в DataFrame.

func.start_message(bot)  # Импорт функции приветственного сообщения.

func.text_message(bot)  # Импорт функции входящих сообщений от пользователя.

bot.polling(none_stop=True, interval=0)  # Функция опроса сервера Telegrame на предмет новых сообщений.
