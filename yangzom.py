
import telebot

bot = telebot.TeleBot('6414409961:AAHNYzgBLgitjx6zJ1Aiq1dEnKWY0lxlSxc')


@bot.message_handler(commands=["start"])

def start(m, res=False):

    bot.send_message(m.chat.id, 'Бот запущен. Начните общение с ним.')


@bot.message_handler(content_types=["text"])

def handle_text(message):

    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)

bot.polling(none_stop=True, interval=0)