import telebot  # Добавляем библиотеку telebot для создания Телеграмм-бота.
import settings
import func

bot = telebot.TeleBot(settings.TOKEN)  # Создание бота c использованием ключа Telegrame.

position_out = func.position_output()

start = func.handle_start(message)

message_text = func.handle_text()

bot.polling(none_stop=True, interval=0)  # Функция опроса сервера Telegrame на предмет новых сообщений.
