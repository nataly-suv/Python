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

# стартовое меню, с выбором функционала


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


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


''' Блок для просмотра всей телефонной книги '''


def show(update, context):
    conn = sqlite3.connect(
        '10_Seminar_DZ_9/Task_063_DZ-9/fonebook.db')  # подгружаем базу
    cursor = conn.cursor()
    cursor.execute("select * from fonebook")  # select * - выбрать все
    results = cursor.fetchall()
    context.bot.send_message(update.effective_chat.id,
                             f"{results}")  # выводим в бот


''' Блок для показа конкретного человека '''

# Запрашиваем информацию


def show_person(update, context):
    context.bot.send_message(update.effective_chat.id,
                             f"Введите фамилию: \n Для выхода напишите /stop")
    return 1

# Обрабатываем запрос


def show_person_out(update, context):
    conn = sqlite3.connect('10_Seminar_DZ_9/Task_063_DZ-9/fonebook.db')
    cursor = conn.cursor()
    text = update.message.text  # считали из бота
    cursor.execute(
        f"select * from fonebook where firs_name like '%{text}%'")
    results = cursor.fetchall()
    update.message.reply_text(f"{results}")


# объединяем запрос информации и обработку информации в один диалог
show_person_handler = ConversationHandler(
    # входная точка
    # попадаем сюда при вводе в боте /show_person
    entry_points=[CommandHandler('show_person', show_person)],

    # Состояние внутри диалога.
    states={
        # обработка запроса в функции show_person_out
        1: [MessageHandler(Filters.text & ~Filters.command, show_person_out)],
    },

    # Точка прерывания диалога. В данном случае — команда /stop.
    fallbacks=[CommandHandler('stop', stop)]
)


''' Блок для удаления записи '''

# Запрашиваем информацию


def del_note(update, context):
    context.bot.send_message(
        update.effective_chat.id, f"Введите индекс для удаления: \n Для выхода напишите /stop")
    return 1

# Обрабатываем запрос


def del_note_out(update, context):
    conn = sqlite3.connect('10_Seminar_DZ_9/Task_063_DZ-9/fonebook.db')
    cursor = conn.cursor()
    text = update.message.text   # считали из бота
    cursor.execute(
        f"delete from fonebook where id={text}")
    conn.commit()
    update.message.reply_text(f"информация удалена")


# объединяем запрос информации и обработку информации в один диалог
del_note_handler = ConversationHandler(
    # входная точка
    # попадаем сюда при вводе в боте /del_note
    entry_points=[CommandHandler('del_note', del_note)],

    # Состояние внутри диалога.
    states={
        # обработка запроса в функции del_note_out
        1: [MessageHandler(Filters.text & ~Filters.command, del_note_out)],
    },

    # Точка прерывания диалога. В данном случае — команда /stop.
    fallbacks=[CommandHandler('stop', stop)]
)


''' Блок для удаления записи '''

# Запрашиваем информацию


def add_note(update, context):
    context.bot.send_message(
        update.effective_chat.id, f"Введите данные для добавления: \n Для выхода напишите /stop")
    return 1

# Обрабатываем запрос


def add_note_out(update, context):
    conn = sqlite3.connect('10_Seminar_DZ_9/Task_063_DZ-9/fonebook.db')
    cursor = conn.cursor()
    text = update.message.text  # считали из бота
    text = text.split()  # разделили строки по пробелу на список строк
    cursor.execute(
        f"insert into fonebook (firs_name, second_name, father_name, fone, description)"
        f"values ('{text[0]}', '{text[1]}', '{text[2]}', '{text[3]}', '{text[4]})')")
    conn.commit()
    update.message.reply_text(f"информация добавлена")


# объединяем запрос информации и обработку информации в один диалог
add_note_handler = ConversationHandler(
    # попадаем сюда при вводе в боте /add_note
    entry_points=[CommandHandler('add_note', add_note)],

    # Состояние внутри диалога.
    states={
        # обработка запроса в функции add_note_out
        1: [MessageHandler(Filters.text & ~Filters.command, add_note_out)],
    },

    # Точка прерывания диалога. В данном случае — команда /stop.
    fallbacks=[CommandHandler('stop', stop)]
)


'Регистрируем все обработчики и передаем их в диспетчер'

start_handler = CommandHandler('start', start)  # стартовое меню
show_handler = CommandHandler('show', show)    # показ всей книги


dispatcher.add_handler(start_handler)  # стартовое меню
dispatcher.add_handler(show_handler)    # показ всей книги
dispatcher.add_handler(show_person_handler)    # показ конкретного человека
dispatcher.add_handler(del_note_handler)    # удаление записи
dispatcher.add_handler(add_note_handler)    # добавление записи


updater.start_polling()
updater.idle()
