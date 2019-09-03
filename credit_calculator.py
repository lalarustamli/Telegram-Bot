import numpy
import bot
from time import sleep


def credit_calculator(assurance, months, amount):
    """Return monthly and final amount based on <assurance>, <months>, <amount>.
    """
    if assurance:
        monthly = -numpy.pmt(0.23 / 12, months, amount)
    else:
        monthly = -numpy.pmt(0.25 / 12, months, amount)

    final_amount = round(monthly * months, 2)
    monthly = round(monthly, 2)

    response = {"final_amount": final_amount, "monthly": monthly}

    return response

def ask_credit_calculator_details(chat_id,update_id,step=0):
    """Ask credit details (credit_assurance, credit_months, credit_amount)
    from user and calculate (final_amount)
    """
    new_values = {'$set': {}}
    sender = {'sender_id': chat_id,
              'user_data': {}}
    # bot.back_to_menu(chat_id,update_id)
    message="Kredit sifarişi blokuna daxil olmusunuz. Təminatlıdır?"
    commands=["Təminatlıdır", "Təminatlı Deyil","Geriyə qayıt"]
    reply_markup= bot.reply_markup_maker(commands)
    bot.send_message(chat_id,message,reply_markup)
    chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
    bot.insert_sender(sender)
    while text.lower() == 'kredit':
        chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
        sleep(0.5)
    if text==commands[0]:
        new_values['$set']['user_data.credit_assurance'] = True
        sender= bot.update_sender(sender,new_values)
        print('True')
    elif text==commands[1]:
        new_values['$set']['user_data.credit_assurance'] =False
        sender= bot.update_sender(sender, new_values)
        print('False')
    elif text==commands[2]:
        bot.menu(chat_id,text,update_id)
        return
    print(text)
    message="Kredit müddəti neçə aydır?"
    commands=['12','24','36','Geriyə qayıt']
    reply_markup= bot.reply_markup_maker(commands)
    bot.send_message(chat_id, message,reply_markup)
    chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
    while text=="Təminatlıdır":
        chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
        sleep(0.5)
    if text in commands:
        if text == commands[3]:
            bot.menu(chat_id,text,update_id)
        else:
            new_values['$set']['user_data.credit_months'] = text
            sender= bot.update_sender(sender, new_values)
            message="Kredit məbləği nə qədərdir?"
            bot.send_message(chat_id, message, reply_markup=None)
            chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
            while text == "Kredit məbləği nə qədərdir?":
                chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
                sleep(0.5)
            if text:
                new_values['$set']['user_data.credit_amount'] = text
                sender = bot.update_sender(sender, new_values)
                calculated_credit = credit_calculator(sender['user_data']['credit_assurance'],
                                                  int(sender['user_data']['credit_months']),
                                                  int(text))
                new_values['$set']['user_data.credit_monthly'] = calculated_credit['monthly']
                new_values['$set']['user_data.credit_final_amount'] = calculated_credit['final_amount']
                sender= bot.update_sender(sender,new_values)
                print(calculated_credit)
                monthly=calculated_credit['monthly']
                final_amount=str(calculated_credit['final_amount'])
                message=f'{final_amount} məbləğində sifarişiniz qeydə alındı. Rəsmiləşdirmək istəyirsiniz?'
                commands=["Bəli","Xeyr"]
                reply_markup= bot.reply_markup_maker(commands)
                bot.send_message(chat_id,message,reply_markup)
                chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
                if text==commands[0]:
                    print('beli')
                    ask_credit_details(chat_id,update_id)
                    return
                else:
                    bot.menu(chat_id,text,update_id)

def ask_credit_details(chat_id,update_id):
    """ Ask user's information (user_name, user_surname, user_phone, user_company,
    user_credit_amount, user_reason) so as to confirm borrowing credit
    """
    new_values = {'$set': {}}
    sender = {'sender_id': chat_id,
              'user_data': {}}
    bot.insert_sender(sender)
    questions = ["Zəhmət olmasa adınızı daxil edin","Zəhmət olmasa soyadınızı daxil edin","Zəhmət olmasa telefon nömrənizi daxil edin",
                 "İşlədiyiniz təşkilatin adını daxil edin","Kredit götürmək istədiyiniz məbləği daxil edin","Krediti nə üçün götürmək istəyirsiniz?",
                 "Sizin kredit sorğunuz qeydə alındı, təşəkkürlər. Tezliklə sizə cavab veriləcək."]
    columns = ["user_name","user_surname","user_phone","user_company","user_credit_amount","user_reason"]

    for i in range(len(questions)):
        message = questions[i]
        bot.send_message(chat_id,message)
        if i != len(questions) - 1:
            chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
            while text == questions[i]:
                chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
                sleep(0.5)
            if text:
                if columns[i] == "user_phone":
                    while True:
                        try:
                            new_values['$set']['user_data.amount'] = int(text)
                            break
                        except ValueError:
                            message = "Zəhmət olmasa, mobil nömrənizi rəqəmlərlə daxil edin, məsələn: 0705505050"
                            bot.send_message(chat_id, message)
                            message = questions[i]
                            bot.send_message(chat_id, message)
                            chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
                else:
                    new_values['$set']['user_data.{}'.format(columns[i])] = text
                    sender = bot.update_sender(sender, new_values)
        else:
            break
