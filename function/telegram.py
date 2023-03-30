import requests
from function import debug
from config import token, chatid

def sendMessage(name, mail, phone):
    if phone == False: 
        return
    
    try:
        response = requests.post(f'https://api.telegram.org/bot{token}/sendMessage', 
        data={
            'chat_id': chatid, 
            'text': 
            "Сообщение с сайта Videosfera!\n\n" + \
            "Имя: " + name + "\n" + \
            "Телефон: " + phone + "\n" + \
            "Эл. почта: " + mail + "\n" + \
            "Skype или профиль VK:" + "\n\n" + \
            "Суть вопроса:\n"
        })

        if response.status_code != 200:
            debug.message("Ошибка отправки в telegram: " + response.text)
            return False

    except requests.exceptions.HTTPError:
        debug.message('Произошла ошибка: ', response.status_code)
        return False
    
    except requests.exceptions.ConnectionError:
        debug.message('Отсутствует подключение к интернету!')
        print('Перепроверяю подключение к интернету. Ожидаю 1 минуту...')
        return "инет"
    
    print("Нормер: " + phone + " успешно отправлен!")
    return True