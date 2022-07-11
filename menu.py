from telegram.ext import ConversationHandler
from buttons import homework


def head_menu(update, context):
    update.message.reply_text(
        text="*Ro'yhatdan o'tib bogansizku*\n"
             "*Proyektlarizi topshiraqolin 😄*",
        parse_mode="Markdown"
    )


def send_message(update, context):
    update.message.reply_text(
        text="Loyihangizni *.zip* fayl ko'rinishida yuboring",
        parse_mode="Markdown"
    )
    return 6


def get_document(update, context):
    global file
    file = update.message.document

    update.message.reply_text("*Lo'yihangiz haqida qisqacha feedback yozing*",
                              parse_mode="Markdown")
    return 7


def get_feedback(update, context):
    global text
    text = update.message.text

    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name

    context.bot.send_document(chat_id=392330197,
                              document=file)

    update.message.bot.send_message(chat_id=392330197,
                                    text=f"O'quvchi *{first_name} {last_name}* \n"
                                         f"\n*Loyiha haqida feedback:* \n"
                                         f"{text}",
                                    parse_mode="Markdown")
    update.message.reply_text(
        text="*Loyihangizni Komiljon aka ga yubordim. Ko'rib chiqib javobini sizga tez orada yuboradi*",
        reply_markup=homework, parse_mode="Markdown"
    )

    return ConversationHandler.END
