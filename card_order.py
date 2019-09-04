import bot
import credit_calculator
from time import sleep
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def card_order(chat_id, update_id):
    sender = {'sender_id': chat_id,
              'user_data': {}}
    commands = ['sifariş et', 'faizlər və ödəniş', 'harada keçir','geriyə qayıt']
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
        commands = ["partnyor təklifi","geriyə qayıt"]
        reply_markup = bot.reply_markup_maker(commands)
        bot.send_message(chat_id, message, reply_markup)
        chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
        if text.lower() == commands[0]:
            message = 'BirKart taksit kartı partnyorları siyahısına yeni partnyorun əlavə olunması ilə bağlı müraciətinizi aşağıdaki linkdən edə bilərsiniz:' + url_partner
            bot.send_message(chat_id, message, reply_markup=None)
            chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
        elif text.lower() == commands[1]:
            card_order(chat_id, update_id)
    elif text.lower() == commands[3]:
        bot.menu(chat_id, text, update_id)




url_partner = 'https://birkart.az/online-order/advise-partner'
eligibility = "Salam Hörmətli müştəri. Hal-hazırda BirKart-ın taksit pratnyorları sırasında 1000-dən çox brend, 2000-dən çox mağaza mövcuddur. BirKartla partnyor mağazalarımızda etdiyiniz istənilən alış-verişi öz istəyinizlə 18 ayadək taksitlə ödəyə və ya məbləği kartınızdan birbaşa olaraq sildirə bilərsiniz. Bunun üçün, bu məlumatı ödənişi edən zaman mağazanın kassasında bildirməyiniz yetərlidir. Əgər partnyor olmayan mağazalardan alış-veriş etsəniz bu zaman kartınızdan çıxılan məbləğ aylara bölünmür və siz 40 günədək müddətdə vəsaiti kartınıza əlavə faiz/komissiya olmadan geri qaytarırsınız. Əgər siz istədiyiniz brendin BirKart partnyoru olmasını istəyirsinizsə, aşağıdakı linkə daxil ola bilərsiniz."

def rates_and_payments(chat_id,update_id):
    sender = {'sender_id': chat_id,
              'user_data': {}}
    commands = ['ödənişlər', 'faizlər', 'limitlər','geriyə qayıt']
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
    elif text.lower() == commands[3]:
        card_order(chat_id,update_id)


def payments(chat_id,update_id):
    sender = {'sender_id': chat_id,
              'user_data': {}}
    commands = ['ödəniş hesablama', 'borc öyrənmə', 'borcun ödənişi','geriyə']
    text = "Xidmətlərdən birini seçin"
    reply_markup = bot.reply_markup_maker(commands)
    bot.send_message(chat_id, text, reply_markup)
    chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
    bot.insert_sender(sender)
    if text.lower() == commands[0]:
        message = payment_calculate + cabinet_url
        bot.send_message(chat_id, message, reply_markup=None)
        chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
    if text.lower() == commands[1]:
        commands = ['cif nədir','geriyə']
        message = "BirKart üzrə borcunuzu öyrənmək üçün şəxsi kabinetinizə daxil olun. CİF kodunuzu daxil edərək, borcunuzu öyrənə bilərsiniz. https://birkart.az/cabinet/&%20"
        reply_markup = bot.reply_markup_maker(commands)
        bot.send_message(chat_id,message,reply_markup)
        chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
        if text.lower() == commands[0]:
            message = cif
            commands = ['geriyə']
            reply_markup = bot.reply_markup_maker(commands)
            bot.send_message(chat_id, message, reply_markup)
            chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
            if text.lower() == commands[0]:
                payments(chat_id,update_id)
        if text.lower() == commands[1]:
            payments(chat_id,update_id)
    if text.lower() == commands[2]:
        message = "Linkə daxil olub borcu ödəyə bilərsiniz : https://pay.kapitalbank.az/"
        bot.send_message(chat_id, message, reply_markup=None)
    if text.lower()==commands[3]:
        card_order(chat_id,update_id)




payment_calculate="Aylıq hesablanmış minimal məbləğ əsas borc və faiz borcundan ibarətdir və etdiyiniz əməliyyat növünə görə fərqlənir. Əsas borc kartın balansına yatırılır, faiz borcu isə - xeyr. Zəhmət olmasa, ödənişlərinizi şəxsi kabinetdə izləyərdiniz. "
cabinet_url = "https://birkart.az/cabinet/&%20"
cif = "CIF kod Sizin BirKart-ın/Kreditin aylıq ödənişlərini etmək və şəxsi kabinetə daxil olmaq üçün fərdi koddur. CIF kodunuzu BirBank tətbiqdən (adınız altında olan “Məlumatlarıma baxmaq” bölümdə), BirKart/Kredit müqavilənizdən və ya Sizə ən yaxın filialdan əldə edə bilərsiniz."

def interest_rates(chat_id,update_id):
    sender = {'sender_id': chat_id,
              'user_data': {}}
    commands = ['nağdlaşma', 'partnyor mağazalar', 'digər mağazalar','geriyə']
    text = "Xidmətlərdən birini seçin"
    reply_markup = bot.reply_markup_maker(commands)
    bot.send_message(chat_id, text, reply_markup)
    chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
    bot.insert_sender(sender)
    if text.lower() == commands[1]:
        message = "Partnyor mağazalar -  BirKartla partnyor olduğumuz mağazalarda əməliyyat aparıb, faizsiz taksitlə ödəniş edə bilərsiz. Partnyor mağazalar siyahısı ilə tanış ola bilərsiniz : https://birkart.az/harada-kecerlidir?search=&category=&taksit=0&taksit2=18/&%20"
        commands = ["geriyə"]
        reply_markup=bot.reply_markup_maker(commands)
        bot.send_message(chat_id,message,reply_markup)
    if text.lower() == commands[2]:
        message = other_shops
        commands = ["geriyə"]
        reply_markup = bot.reply_markup_maker(commands)
        bot.send_message(chat_id, message, reply_markup)
    if text.lower() == commands[3]:
        rates_and_payments(chat_id,update_id)

other_shops = "Mağaza qeyri partnyor şəbəkəsinə aid olduqda, əgər Siz bu ay ödəniş etsəz, növbəti ayın 1-10 tarixləri ödəniş vaxtıdır və tam məbləği ödəsəniz faizsiz ödəmə imkanınız olacaq (qeyri taksit). Əgər tam məbləği Siz növbəti ayın 1-10 tarixində ödəniş edə bilməsəz, məbləğin ən azı 5% və hesablanmış komissiyası günlər üzrə (illik faiz dərəcəsi 25%lə) ödəniş edə bilərsiniz. Qalıq borcu isə gələn aya keçirə bilərsiniz."

def limits(chat_id,update_id):
    sender = {'sender_id': chat_id,
              'user_data': {}}
    commands = ['maaşa uyğun limit', 'birkart limiti', 'limit artırmaq','geriyə']
    text = "Xidmətlərdən birini seçin"
    reply_markup = bot.reply_markup_maker(commands)
    bot.send_message(chat_id, text, reply_markup)
    chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
    bot.insert_sender(sender)
    if text.lower() == commands[1]:
        message = "Birkart kredit kartı üzrə limit 100 AZN-dən - 10 000 AZN-ə kimi olur, hər müştərinin maliyyə durumuna uyğun kredit limiti ayrılır."
        commands = ["maaşa görə hesabla", "geriyə"]
        reply_markup = bot.reply_markup_maker(commands)
        bot.send_message(chat_id,message,reply_markup)
        
