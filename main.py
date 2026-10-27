import telebot

bot = telebot.TeleBot("8844783446:AAHpcC1yuhF8ibsQPfth2VtdGlf_75OE7KI")

@bot.message_handler(commands = ["start"])
def start(message):
    print("start")
    bot.reply_to(message, "Бот Посох Судьбы 🔮")

@bot.message_handler(commands = ["hello", "hi", "Hello", "Hi", "HELLO", "HI"])
def greeting(message):
    print("hello")
    bot.reply_to(message, "Привет! Добро пожаловать в чат с 'Посохом Судьбы'.")

@bot.message_handler(commands = ["stop", "bye", "goodbye"])
def stop(message):
    print("stop")
    bot.reply_to(message, "Посох Судьбы ждёт тебя. Не забывай что есть у нас скидки от 30 до 20% чайник за 2000 рублей!")

#bot.message_handler() (start)

bot.polling(non_stop = True, interval = 0)
