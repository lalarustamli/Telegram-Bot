import requests
import json
from time import sleep
from connect import find_sender, insert_sender, update_sender
import cards
import requirements
import card_order
import credit_calculator

token = '883097133:AAHbEkxKfVPSr1xfye_Fdo-iKZvdVvuPd_8'
url = 'https://api.telegram.org/bot{}/'.format(token)


def getme():
    res = requests.get(url + "getme")
    d = res.json()
    username = d['result']['username']

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates(offset=None):
    while True:
        try:
            URL = url + 'getUpdates'
            if offset:
                URL += '?offset={}'.format(offset)

            res = requests.get(URL)
            while (res.status_code != 200 or len(res.json()['result']) == 0):
                sleep(1)
                res = requests.get(URL)
            print(res.url)
            return res.json()

        except:
            pass;


def send_message(chat_id, text, reply_markup=None):
    URL = url + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup:
        URL += '&reply_markup={}'.format(reply_markup)
    res = requests.get(URL)
    while res.status_code != 200:
        res = requests.get(URL)
    print(res.status_code)


def get_last(data):
    results = data['result']
    count = len(results)
    last = count - 1
    last_update = results[last]
    print(last_update)
    return last_update


def get_last_id_text(updates):
    last_update = get_last(updates)
    chat_id = last_update['message']['chat']['id']
    update_id = last_update['update_id']
    try:
        text = last_update['message']['text']
    except:
        text = ''
    return chat_id, text, update_id

def get_last_user_info(updates):
    last_update=get_last(updates)
    chat_id = last_update['message']['chat']['id']
    first_name=last_update['message']['chat']['first_name']
    username=last_update['message']['chat']['username']
    try:
        text = last_update['message']['text']
    except:
        text = ''
    user_info = {
        'chat_id':chat_id,
        'first_name':first_name,
        'username':username,
        'text':text
    }
    return user_info




def ask_contact(chat_id):
    print('Ask Contact')
    text = 'Send Contact'
    keyboard = [[{"text": "Contact", "request_contact": True}]]
    reply_markup = {"keyboard": keyboard, "one_time_keyboard": True}
    send_message(chat_id, text, json.dumps(reply_markup))



def reply_markup_maker(data):
    keyboard = []
    for i in range(0, len(data), 2):
        key = []
        key.append(data[i].title())
        try:
            key.append(data[i + 1].title())
        except:
            pass
        keyboard.append(key)

    reply_markup = {"keyboard": keyboard, "one_time_keyboard": True}
    return json.dumps(reply_markup)


def welcome_note(chat_id, commands):
    text = "Salam"
    send_message(chat_id, text)
    text = 'Xidmətlərdən birini seçin'
    reply_markup = reply_markup_maker(commands)
    send_message(chat_id, text, reply_markup)


def start(chat_id):
    message = 'Başlayaq?'
    reply_markup = reply_markup_maker(['başla'])
    send_message(chat_id, message, reply_markup)

    chat_id, text, update_id = get_last_id_text(get_updates())
    while (text.lower() != 'başla'):
        chat_id, text, update_id = get_last_id_text(get_updates(update_id + 1))
        sleep(0.5)

    return chat_id, text, update_id


def end(chat_id, text, update_id):
    message = 'Əməliyyatı dayandırmaq istəyirsiniz?'
    reply_markup = reply_markup_maker(['Bəli', 'Xeyr, davam edək'])
    send_message(chat_id, message, reply_markup)

    new_text = text
    while (text == new_text):
        chat_id, new_text, update_id = get_last_id_text(get_updates(update_id + 1))
        sleep(1)

    if new_text == 'Bəli':
        return 'y'
    else:
        return 'n'


def menu(chat_id, text, update_id):
    commands = ['kart növləri','tələblər və sənədlər', 'kart sifarişi', 'məzənnə']
    text = "Xidmətlərdən birini seçin"
    reply_markup = reply_markup_maker(commands)
    send_message(chat_id, text, reply_markup)
    while (text.lower() == 'başla' or text.lower() == 'geriyə qayıt' ):
        chat_id, text, update_id = get_last_id_text(get_updates(update_id + 1))
        sleep(0.5)
    print(text)
    while text.lower() not in commands:
        chat_id, text, update_id = get_last_id_text(get_updates(update_id + 1))
        sleep(0.5)
    if text.lower() == 'kart növləri':
        cards.cards_info(chat_id,update_id)
    if text.lower() == 'tələblər və sənədlər':
        requirements.requirements_menu(chat_id,update_id)
    if text.lower() == 'kart sifarişi':
        card_order.card_order(chat_id,update_id)
    # if text.lower() == 'məzənnə':
    #     currency.ask_iba_currency_calculator_details(chat_id, update_id)

def back_to_menu(chat_id,text,update_id):
    commands = ['Geriyə']
    reply_markup=reply_markup_maker(commands)
    send_message(chat_id,reply_markup)
    if text == commands[0]:
        menu(chat_id,text,update_id)


def main():
    text = ''
    chat_id, text, update_id = get_last_id_text(get_updates())
    chat_id, text, update_id = start(chat_id)
    print('Started')

    while text.lower() != 'y':
        sleep(1)
        text = 'başla'
        menu(chat_id, text, update_id)
        chat_id, text, update_id = get_last_id_text(get_updates())
        text = 'y'
        print(text)
        text = end(chat_id, text, update_id)


if __name__ == '__main__':
    main()