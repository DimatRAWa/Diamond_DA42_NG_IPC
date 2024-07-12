import telebot  # Добавляем библиотеку telebot для создания Телеграмм-бота.
import settings
import func

bot = telebot.TeleBot(settings.TOKEN)  # Создание бота c использованием ключа Telegrame.

func.position_output()

func.start_message(bot)

func.text_message(bot)

bot.polling(none_stop=True, interval=0)  # Функция опроса сервера Telegrame на предмет новых сообщений.
