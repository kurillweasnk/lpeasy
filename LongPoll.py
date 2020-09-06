import vk_api
 
import requests
 
 
 
session = request.Session()
 
login, password = 'Ваш логин, почта и номер', 'Ваш пароль'
 
vk_session = vk_api.VkApi(login, password)
 
try:
 
    vk_session.auth(token_only=True)
 
except vk_api.AuthError as error_msg:
 
    print(error_msg)
 
    return

from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:			
        if event.text == '...' or event.text == 'Второй вариант фразы': #Если написали заданную фразу
            if event.from_user: #Если написали в ЛС
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    message='Ваш текст'
		)
            elif event.from_chat: #Если написали в Беседе
                vk.messages.send( #Отправляем собщение
                    chat_id=event.chat_id,
                    message='Балабол точками'
import datetime
vk.messages.send(
    user_id=event.user_id,
    message='Московское время: ' + str(now.strftime("%H:%M"))
attachments = []
from vk_api import VkUpload 
upload = VkUpload(vk_session)
image_url = 'Ссылка на картинку'
image = session.get(image_url, stream=True)
photo = upload.photo_messages(photos=image.raw)[0]
attachments.append(
    'photo{}_{}'.format(photo['owner_id'], photo['id'])
)
vk.messages.send(
    user_id=event.user_id,
    attachment=','.join(attachments),
    message='И зачем мне это🤔'

import wikipedia #Модуль Википедии
wikipedia.set_lang("RU")
if event.text == '.вики' or event.text == 'Вики' or event.text == '.Вики' or event.text == 'вики' or event.text == '. вики' or event.text == 'wikipedia' or event.text == 'википедия' or event.text == 'wiki': #если нам пришло сообщение с текстом Википедия или Вики или ... или wiki
    if event.from_user: #Если написали в KC
        vk.messages.send(
            user_id=event.user_id,
            message='Введите запрос' #Пишем "Введите запрос"
	)
    elif event.from_chat: #Если написали в беседе
        vk.messages.send(
            chat_id=event.chat_id,
            message='Введите запрос' #Пишем "Введите запрос"
	)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text: #Пинаем longpoll
            if event.from_user:
                vk.messages.send( #Если написали в ЛС
                    user_id=event.user_id,
                    message='Вот что я нашёл: \n' + str(wikipedia.summary(event.text)) #Пишем "Вот что я нашёл" И то что вернёт нам api Wikipedia по запросу текста сообщения
		)
                break #выходим из цикла
        elif event.from_chat: #Если написали в беседе
            vk.messages.send(
                chat_id=event.chat_id,
                message='Вот что я нашёл: \n' + str(wikipedia.summary(event.text)) #Пишем "Вот что я нашёл" И то что вернёт нам api Wikipedia по запросу текста сообщения
	    )
            break #выходим из цикла
    continue


