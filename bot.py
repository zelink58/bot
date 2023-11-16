import telebot
import parser

#main variables
TOKEN = "6892263065:AAHDiIdT4SaTluUVY6skMRAXpWz9C3Vtmw4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду парсить заголовки с Хабра')
bot.polling()
