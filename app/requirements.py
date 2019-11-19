import bot
import credit_calculator
from time import sleep
def requirements_menu(chat_id, update_id):
    sender = {'sender_id': chat_id,
              'user_data': {}}
    commands = ['kimlər ala bilər', 'hansı sənədlər ', 'birkart ala bilərəm']
    text = "Xidmətlərdən birini seçin"
    reply_markup = bot.reply_markup_maker(commands)
    bot.send_message(chat_id, text, reply_markup)
    chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
    bot.insert_sender(sender)
    while text.lower() == 'tələblər və sənədlər':
        chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
        sleep(0.5)
    if text.lower() == commands[0]:
        message = who_are_eligible
        commands = ["kart sifarişi", "sənəd siyahısı"]
        reply_markup = bot.reply_markup_maker(commands)
        bot.send_message(chat_id, message, reply_markup)
        chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
        if text.lower() == commands[0]:
            credit_calculator.ask_credit_details(chat_id, update_id)
        elif text.lower() == commands[1]:
            message = documents_list
            commands = ["kart sifarişi"]
            reply_markup = bot.reply_markup_maker(commands)
            bot.send_message(chat_id, message, reply_markup)
            chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
            if text.lower() == commands[0]:
                credit_calculator.ask_credit_details(chat_id, update_id)
    if text.lower() ==commands[1]:
        message = documents_list
        commands = ["kart sifarişi"]
        reply_markup = bot.reply_markup_maker(commands)
        bot.send_message(chat_id, message, reply_markup)
        chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
        if text.lower() == commands[0]:
            credit_calculator.ask_credit_details(chat_id, update_id)
    if text.lower() == commands[2]:
        #needs edit
        credit_calculator.ask_credit_details(chat_id, update_id)


who_are_eligible = "İş yerində rəsmi qeydiyyatla çalışan şəxslər yaxud Kapital Bankda əmək haqqı və pensiya kartı olan şəxslər 💳 Yaş həddi - Min. 18 yaş, maks. 67 yaş Son iş yerində staj minimum 6 ay olmalıdır (Kapital Bank müştəriləri üçün 3 ay). Təqaüdçülər üçün isə belə bir tələb yoxdur.  Əgər tələblər sizə uyğundursa, aşağıdan BirKart sifariş edə bilərsiniz:"
documents_list = "BirKart əldə etmək üçün lazım olan sənədlər aşağıdakılardır: ⬇️ 1) Şəxsiyyət Vəsiqəsi 🔖 2) İş yerindən arayış 📜 3) Kapital Bankdan əmək haqqı və ya pensiya kartı (ƏGƏR VARSA) 💳"