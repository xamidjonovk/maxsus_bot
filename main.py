from telegram.ext import (Updater, CommandHandler, ConversationHandler, MessageHandler, Filters)
from buttons import register_button
from register import start_conversation, get_first_name, get_last_name, get_directory, get_contact, submit
from menu import head_menu, get_document, send_message, get_feedback
from admin import admin_id, admin_menu, hashtags, stats, remove


def start(update, context):
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
    updater = Updater(token="5515845639:AAG8jcmMf4Vxt_2LrEGeoOutaj3zUwcV660")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
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
