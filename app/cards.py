import bot
from time import sleep
import credit_calculator


def cards_info(chat_id, update_id):
    sender = {'sender_id': chat_id,
              'user_data': {}}
    commands = ['birkart taksit', 'birkart cashback', 'birkart miles']
    text = "Xidmətlərdən birini seçin"
    reply_markup = bot.reply_markup_maker(commands)
    bot.send_message(chat_id, text, reply_markup)
    chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
    bot.insert_sender(sender)
    while text.lower() == 'kart növləri':
        chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
        sleep(0.5)
    if text.lower() == commands[0]:
        message = taksit_info
        commands = ["kart sifarişi", "tariflər və qiymət"]
        reply_markup = bot.reply_markup_maker(commands)
        bot.send_message(chat_id, message, reply_markup)
        chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
        if text.lower() == commands[0]:
            credit_calculator.ask_credit_details(chat_id, update_id)
        elif text.lower() == commands[1]:
            message = taksit_tarif
            bot.send_message(chat_id, message, reply_markup=None)
    elif text.lower() == commands[1]:
        message = cashback_info
        commands = ["kart sifarişi", "tariflər və qiymət"]
        reply_markup = bot.reply_markup_maker(commands)
        bot.send_message(chat_id, message, reply_markup)
        chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
        if text.lower() == commands[0]:
            credit_calculator.ask_credit_details(chat_id, update_id)
        elif text.lower() == commands[1]:
            message = cashback_tarif
            bot.send_message(chat_id, message, reply_markup=None)
    elif text.lower() == commands[2]:
        message = miles_info
        commands = ["kart sifarişi", "tariflər və qiymət"]
        reply_markup = bot.reply_markup_maker(commands)
        bot.send_message(chat_id, message, reply_markup)
        chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
        if text.lower() == commands[0]:
            credit_calculator.ask_credit_details(chat_id, update_id)
        elif text.lower() == commands[1]:
            message = miles_tarif
            bot.send_message(chat_id, message, reply_markup=None)
    # while text.lower() == 'birkart taksit':
    #     chat_id, text, update_id = bot.get_last_id_text(bot.get_updates(update_id + 1))
    #     sleep(0.5)


taksit_info = '18-67 yaşı, rəsmi gəliri, son iş yerində 6 aylıq iş təcrübəsi olan (Kapital Bank müştəriləri üçün 3 ay) və ya pensiya alan hər kəs BirKart əldə edə bilər.'
taksit_tarif = 'Kart 3 il müddətə aktivdir Bütün partnyor mağazalarda istədiyiniz məhsulu öz qiymətinə, 18 ayadək faizsiz taksitlə əldə edə bilərsiniz.Kartın 1 illik qiyməti 15 AZN-dir. BirKartınızla ilk 90 gün ərzində 3 dəfə minimum 10 AZN-lik nağdsız əməliyyat etdikdə (taksit, onlayn ödəniş, birdəfəlik alış) hesabınızdan kartın 1-ci il üzrə illik ödənişi çıxarılmayacaq.SMS info xidməti pulsuzdur. 📩 Kartla birdəfəlik (nağdsız) ödənişlərdə güzəşt müddəti - 40 günədək'

cashback_info = "Kart 3 il müddətə aktivdir. Bütün partnyor mağazalarda istədiyiniz məhsulu öz qiymətinə, 18 ayadək faizsiz taksitlə əldə edə bilərsiniz. Kartın 1 illik qiyməti 15 AZN-dir. BirKartınızla ilk 90 gün ərzində 3 dəfə minimum 10 AZN-lik nağdsız əməliyyat etdikdə (taksit, onlayn ödəniş, birdəfəlik alış) hesabınızdan kartın 1-ci il üzrə illik ödənişi çıxarılmayacaq. SMS info xidməti pulsuzdur. 📩 Kartla birdəfəlik (nağdsız) ödənişlərdə güzəşt müddəti - 40 günədək"
cashback_tarif = "1.5%-dən 30%-dək cashback imkanı ↩️18 ayadək faizsiz taksit imkanı Kart 3 il müddətə aktivdir. Kartla birdəfəlik (nağdsız) ödənişlərdə güzəşt müddəti - 40 günədək. 💳 SMS info xidməti pulsuzdur 📩 Kartın 1 illik qiyməti 35 AZN-dir. BirKartınızla ilk 90 gün ərzində 5 dəfə minimum 20 AZN-lik nağdsız əməliyyat etdikdə (taksit, onlayn ödəniş, birdəfəlik alış) hesabınızdan kartın 1-ci il üzrə illik ödənişi çıxarılmayacaq."

miles_info = "Sizi buludların üzərinə qaldıran kart. BirKart Miles kartıyla əməliyyatlar edin, qazandığınız milləri istənilən aviabiletə dəyişin. Kartın Depozit funksiyası sizə əlavə millər qazandırsın."
miles_tarif = "Milləri istənilən aviabiletə dəyişmək imkanı 🛫 18 ayadək faizsiz taksit imkanı Kart 3 il müddətə aktivdir 1 illik 35 AZN 💵"
