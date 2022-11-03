from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from random import randint

bot_token = '5580181060:AAGFiCzczf7PDKayIT4umVjhg3ZecIjq4Pk'
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

# pip install python-telegram-bot==13.14
# Updater → Dispatсher → Handlers → start → wait_for_the_end
# Updater - взаимодействие между клиентом и сервером
# Dispatсher - отвечает за вызов обработчика сообщений
# Handlers - обработчики сообщений


def start(update, context):
    context.bot.send_message(update.effective_chat.id, f"Привет! Это калькулятор!\n Выберите рассчет (кг в гр) /convert \n Рассчитать значение выражениями /calc")

def convert(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите колличество килограмм, для выхода напишите /stop ')
    return 1

def convert_output(update, context):
    update.message.reply_text(f'{int(update.message.text) * 1000} грамм')

def calc(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите выражение: ')
    return 1

def calc_output(update, context):
    update.message.reply_text(eval(update.message.text))


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


convert_handler = ConversationHandler(
        entry_points=[CommandHandler('convert', convert)],

        # Состояние внутри диалога.
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, convert_output)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )

calc_handler = ConversationHandler(
        entry_points=[CommandHandler('calc', calc)],

        # Состояние внутри диалога.
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, calc_output)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )

start_handler = CommandHandler('start', start)

dispatcher.add_handler(calc_handler)
dispatcher.add_handler(convert_handler)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()