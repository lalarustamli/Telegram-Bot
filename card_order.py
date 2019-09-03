import bot
import credit_calculator
from time import sleep

def card_order(chat_id, update_id):
    sender = {'sender_id': chat_id,
              'user_data': {}}
    commands = ['sifariş et', 'faizlər və ödəniş', 'harada keçir']
    text = "Xidmətlərdən birini seçin"
    reply_markup = bot.reply_markup_maker(commands)
    bot.send_message(chat_id, text, reply_markup)
    chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
    bot.insert_sender(sender)
    while text.lower() == 'kart sifarişi':
        chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
        sleep(0.5)
    if text.lower() == commands[0]:
        credit_calculator.ask_credit_details(chat_id,update_id)
    elif text.lower() == commands[1]:
        rates_and_payments(chat_id,update_id)
    elif text.lower() == commands[2]:
        message = eligibility
        commands = "partnyor təklifi"
        reply_markup = bot.reply_markup_maker(commands)
        bot.send_message(chat_id, message, reply_markup)




eligibility = "Salam Hörmətli müştəri. Hal-hazırda BirKart-ın taksit pratnyorları sırasında 1000-dən çox brend, 2000-dən çox mağaza mövcuddur. BirKartla partnyor mağazalarımızda etdiyiniz istənilən alış-verişi öz istəyinizlə 18 ayadək taksitlə ödəyə və ya məbləği kartınızdan birbaşa olaraq sildirə bilərsiniz. Bunun üçün, bu məlumatı ödənişi edən zaman mağazanın kassasında bildirməyiniz yetərlidir. Əgər partnyor olmayan mağazalardan alış-veriş etsəniz bu zaman kartınızdan çıxılan məbləğ aylara bölünmür və siz 40 günədək müddətdə vəsaiti kartınıza əlavə faiz/komissiya olmadan geri qaytarırsınız. Əgər siz istədiyiniz brendin BirKart partnyoru olmasını istəyirsinizsə, aşağıdakı linkə daxil ola bilərsiniz."

def rates_and_payments(chat_id,update_id):
    sender = {'sender_id': chat_id,
              'user_data': {}}
    commands = ['ödənişlər', 'faizlər', 'limitlər']
    text = "Xidmətlərdən birini seçin"
    reply_markup = bot.reply_markup_maker(commands)
    bot.send_message(chat_id, text, reply_markup)
    chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
    bot.insert_sender(sender)
    while text.lower() == 'faizlər və ödəniş':
        chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
        sleep(0.5)
    if text.lower() == commands[0]:
        payments(chat_id,update_id)
    elif text.lower() == commands[1]:
        interest_rates(chat_id,update_id)
    elif text.lower() == commands[2]:
        limits(chat_id, update_id)


def payments(chat_id,update_id):
    sender = {'sender_id': chat_id,
              'user_data': {}}
    commands = ['ödəniş hesablama', 'borc öyrənmə', 'borcun ödənişi']
    text = "Xidmətlərdən birini seçin"
    reply_markup = bot.reply_markup_maker(commands)
    bot.send_message(chat_id, text, reply_markup)
    chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
    bot.insert_sender(sender)

def interest_rates(chat_id,update_id):
    sender = {'sender_id': chat_id,
              'user_data': {}}
    commands = ['nağdlaşma', 'parnyor mağazalar', 'digər mağazalar']
    text = "Xidmətlərdən birini seçin"
    reply_markup = bot.reply_markup_maker(commands)
    bot.send_message(chat_id, text, reply_markup)
    chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
    bot.insert_sender(sender)

def limits(chat_id,update_id):
    sender = {'sender_id': chat_id,
              'user_data': {}}
    commands = ['maaşa uyğun limit', 'birkart limiti', 'limit artırmaq']
    text = "Xidmətlərdən birini seçin"
    reply_markup = bot.reply_markup_maker(commands)
    bot.send_message(chat_id, text, reply_markup)
    chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
    bot.insert_sender(sender)