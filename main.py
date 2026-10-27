import telebot

bot = telebot.TeleBot("8844783446:AAHpcC1yuhF8ibsQPfth2VtdGlf_75OE7KI")

def start(message):
    print("start")
    bot.reply_to(message, " ")



bot.message_handler() (start)

bot.polling(non_stop = True, interval = 0)
