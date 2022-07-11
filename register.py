from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from buttons import directory, contact, homework, check
from database import update_db


def start_conversation(update, context):
    update.message.reply_text(text="*Ismingizni kiriting*",
                              parse_mode="Markdown",
                              reply_markup=ReplyKeyboardRemove())
    return 1


def get_first_name(update, context):
    message = update.message.text
    context.user_data['first_name'] = message

    update.message.reply_text(
        text="*Familiyangizni kiriting*:",
        parse_mode="Markdown")
    return 2


def get_last_name(update, context):
    message = update.message.text
    context.user_data['last_name'] = message

    update.message.reply_text(
        text="*Yo'nalishingizni tanlang*:",
        reply_markup=directory,
        parse_mode="Markdown")
    return 3


def get_directory(update, context):
    message = update.message.text
    context.user_data['directory'] = message

    update.message.reply_text(
        text="*Telefon raqamingizni yuboring*",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardMarkup(contact, resize_keyboard=True)
    )
    return 4


def get_contact(update, context):
    contract = update.message.text
    context.user_data["contact"] = update.message.contact.phone_number
    name_1 = context.user_data['first_name']
    name_2 = context.user_data['last_name']
    study = context.user_data['directory']
    phone = context.user_data['contact']

    update.message.reply_text(
        text=f"Ma'lumotlaringizni tekshiring va to'griligini tasdiqlang \n"
             f"\nIsm: *{name_1}* \n"
             f"\nFamiliya: *{name_2}* \n"
             f"\nYo'nalish: *{study}* \n"
             f"\nTelefon raqam: *{phone}*",
        parse_mode="Markdown",
        reply_markup=check
    )
    return 5


def submit(update, context):
    name_1 = context.user_data['first_name']
    name_2 = context.user_data['last_name']
    study = context.user_data['directory']
    phone = context.user_data['contact']
    username = update.message.from_user.username
    user_id = update.message.from_user.id

    update_db(name_1, name_2, study, phone, username, user_id)

    update.message.reply_text(
        text="Ro'yhatdan muvaffaqiyatli o'tdingiz",
        parse_mode="Markdown",
        reply_markup=homework
    )
    return ConversationHandler.END
