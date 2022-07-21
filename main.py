from telegram.ext import (Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, )
from buttons import register_button
from register import start_conversation, get_first_name, get_last_name, get_directory, get_contact, submit
from menu import head_menu, get_document, send_message, get_feedback
from admin import admin_id, admin_menu, hashtags, stats, remove
from telegram import ReplyKeyboardRemove

TOKEN = '5478251925:AAFCohl2ROk61S6oJTCwBHGTo5x3HFBodbw'

def stop(update, context):
    update.message.reply_text(text='stopped', reply_markup=ReplyKeyboardRemove())

def start(update, context):
    if update.message.chat.type == "supergroup":
        update.message.reply_text(text="Ro'yxatdan o'tish uchun ushbu botga shaxsiydan start bosing.")
    else:
        user_id = update.message.from_user.id
        if user_id == admin_id:
            admin_menu(update, context)
        elif context.user_data.get("first_name"):
            head_menu(update, context)
        else:
            user = update.message.from_user.first_name
            update.message.reply_text(f"Salom *{user}* \n"
                                      f"*Botdan foydalanish uchun ro'yhatdan o'ting*",
                                      reply_markup=register_button,
                                      parse_mode="Markdown")


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('stop', stop))
    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[MessageHandler(Filters.regex('(Ro\'yhatdan o\'tish)'), start_conversation)],
            states={
                1: [MessageHandler(Filters.text, get_first_name)],
                2: [MessageHandler(Filters.text, get_last_name)],
                3: [MessageHandler(Filters.text, get_directory)],
                4: [MessageHandler(Filters.contact, get_contact)],
                5: [MessageHandler(Filters.text, submit)],
            },
            fallbacks=[CommandHandler('stop', start)]
        )
    )
    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[MessageHandler(Filters.regex("(📚Proyektni topshirish)"), send_message)],
            states={
                6: [MessageHandler(Filters.document, get_document)],
                7: [MessageHandler(Filters.text, get_feedback)]
            },
            fallbacks=[CommandHandler('stop', start)]
        )
    )
    dispatcher.add_handler(MessageHandler(Filters.regex("(📈Statistika)"), stats))
    dispatcher.add_handler(MessageHandler(Filters.regex("(Statistikani yangilash)"), remove))
    dispatcher.add_handler(MessageHandler(Filters.text, hashtags))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
