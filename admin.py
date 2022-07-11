from buttons import admin_buttons

admin_id = 392330197  # 392330197


def admin_menu(update, context):
    update.message.reply_text(
        text="Assalom alekum *Komiljon aka*\n"
             "*Statistika bo'limiga xush kelibsiz😊*",
        reply_markup=admin_buttons,
        parse_mode="Markdown"
    )


agile_data = []
helpme_data = []
hero_data = []

super_hero = {"name": "", "count": 0}
super_agile = {"name": "", "count": 0}
super_helpme = {"name": "", "count": 0}


def hashtags(update, context):
    context.user_data["first_name"] = update.message.from_user.first_name

    if update.message.chat.type == "group":
        message = update.message.text
        if "#agile" in message:
            if context.user_data["first_name"] not in agile_data:
                context.user_data['agile'] = 1
                agile_data.append(context.user_data["first_name"])
                if super_agile["count"] < context.user_data['agile']:
                    super_agile["count"] = context.user_data['agile']
                    super_agile["name"] = context.user_data["first_name"]

            else:
                context.user_data['agile'] += 1
                if super_agile["count"] < context.user_data['agile']:
                    super_agile["count"] = context.user_data['agile']
                    super_agile["name"] = context.user_data["first_name"]
            print(super_agile)
        elif "#helpme" in message:
            if context.user_data["first_name"] not in helpme_data:
                context.user_data['helpme'] = 1
                helpme_data.append(context.user_data["first_name"])
                if super_helpme["count"] < context.user_data['helpme']:
                    super_helpme["count"] = context.user_data['helpme']
                    super_helpme["name"] = context.user_data["first_name"]
            else:
                context.user_data['helpme'] += 1
                if super_helpme["count"] < context.user_data['helpme']:
                    super_helpme["count"] = context.user_data['helpme']
                    super_helpme["name"] = context.user_data["first_name"]
            print(super_helpme)
        elif "#hero" in message:
            if context.user_data["first_name"] not in hero_data:
                context.user_data['hero'] = 1
                hero_data.append(context.user_data["first_name"])
                if super_hero["count"] < context.user_data['hero']:
                    super_hero["count"] = context.user_data['hero']
                    super_hero["name"] = context.user_data["first_name"]
            else:
                context.user_data['hero'] += 1
                if super_hero["count"] < context.user_data['hero']:
                    super_hero["count"] = context.user_data['hero']
                    super_hero["name"] = context.user_data["first_name"]
            print(super_hero)


def stats(update, context):
    update.message.reply_text(text=f"Eng ko'p herolar soni: {super_hero['name']} - {super_hero['count']}\n"
                                   f"Eng ko'p agilelar soni: {super_agile['name']} - {super_agile['count']}\n"
                                   f"Eng ko'p helpmelar soni: {super_helpme['name']} - {super_helpme['count']}")


def remove(update, context):
    global super_hero, super_agile, super_helpme
    super_hero = {"name": "", "count": 0}
    super_agile = {"name": "", "count": 0}
    super_helpme = {"name": "", "count": 0}
    update.message.reply_text(text="Statistika yangilandi")
