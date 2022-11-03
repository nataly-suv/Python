import sqlite3  # иморт sqlite3

from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from random import randint

# создаем коннект с файлом базы данных
# conn = sqlite3.connect('10_Seminar_DZ_9/Task_063_DZ-9/fonebook.db')
# cursor = conn.cursor()

bot_token = '5635214848:AAF0I-MPlXEC-CfTy395lT3Teb2ft9AePz4'
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        f"Привет! Это телефонный справочник!\n"
        f"Выберите необходимое действие:\n"
        f"показать все /show \n"
        f"показать конкретного человека /show_person\n"
        f"удалить запись /del_note\n"
        f"добавить запись /add_note\n"
    )


# # показать всех студентов
# cursor.execute("select * from fonebook")
# results = cursor.fetchall()
# print(results)

def show(update, context):
    conn = sqlite3.connect('10_Seminar_DZ_9/Task_063_DZ-9/fonebook.db')
    cursor = conn.cursor()
    cursor.execute("select * from fonebook")
    results = cursor.fetchall()
    context.bot.send_message(update.effective_chat.id, f"{results}")


# # поиск записи
# surname = 'Иванов'
# cursor.execute(f"select * from students where surname like '%{surname}%'")
# results = cursor.fetchall()
# print(results)

def show_person(update, context):
    context.bot.send_message(update.effective_chat.id, f"Введите фамилию: \n Для выхода напишите /stop")
    return 1

def show_person_out(update, context):
    conn = sqlite3.connect('10_Seminar_DZ_9/Task_063_DZ-9/fonebook.db')
    cursor = conn.cursor()
    text = update.message.text
    cursor.execute(
        f"select * from fonebook where firs_name like '%{text}%'")
    results = cursor.fetchall()
    update.message.reply_text(update.message.text, f"{results}")


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


show_person_handler = ConversationHandler(
        entry_points=[CommandHandler('show_person', show_person)],

        # Состояние внутри диалога.
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, show_person_out)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )







start_handler = CommandHandler('start', start)
show_handler = CommandHandler('show', show)
# show_person_handler = CommandHandler('show_person', show_person)

# info_handler = CommandHandler('info', info)
# roll_handler = CommandHandler('roll', roll)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(show_handler)
dispatcher.add_handler(show_person_handler)



# dispatcher.add_handler(info_handler)
# dispatcher.add_handler(roll_handler)
updater.start_polling()
updater.idle()
