import vk_api
import requests
from config import access_token
import datetime
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randrange
import json

session = vk_api.VkApi(token=access_token)
# long_pool = VkLongPoll(session) #возникает ошибка access denied: no access to call this method


def write_messages(user_id, message):
    '''Отправка сообщений пользователю'''
    return session.method('messages.send', {'user_id': user_id,
                                            'message': message,
                                            'random_id': randrange(2147483647)
                                            })
# print(write_messages(674830336, 'почему ты не отправляешься?!'))
def get_users_name(user_id):
    '''Получить имя пользователя'''
    url = f'https://api.vk.com/method/users.get'
    parameters = {'access_token': access_token,
                  'user_ids': user_id,
                  'v': 5.131}
    result = requests.get(url, params=parameters)
    response = result.json()
    try:
        info_from_dict = response['response']
        for i in info_from_dict:
            first_name = i.get('first_name')
            return first_name
    except KeyError:
        write_messages(user_id, 'Receiving token error, please re-enter the token.')

# print(get_users_name(674830336))


def get_photos(owner_id, offset=0, count=3):
    api_ = requests.get('https://api.vk.com/method/photos.getAll', params={
        'owner_id': owner_id,
        'offset': offset,
        'count': count,
        'access_token': access_token,
        'extended': 1,
        'v': 5.131
    })
    return json.loads(api_.text)


# print(get_photos(674830336))

def get_photos_id(user_id):
    """ПОЛУЧЕНИЕ ID ФОТОГРАФИЙ С РАНЖИРОВАНИЕМ В ОБРАТНОМ ПОРЯДКЕ"""
    url = 'https://api.vk.com/method/photos.getAll'
    params = {'access_token': access_token,
              'owner_id': user_id,
              'extended': 1,
              'count': 25,
              'v': '5.131'}
    resp = requests.get(url, params=params)
    dict_photos = dict()
    resp_json = resp.json()
    try:
        dict_1 = resp_json['response']
        list_1 = dict_1['items']
        for i in list_1:
            photo_id = str(i.get('id'))
            i_likes = i.get('likes')
            if i_likes.get('count'):
                likes = i_likes.get('count')
                dict_photos[likes] = photo_id
        list_of_ids = sorted(dict_photos.items(), reverse=True)
        return list_of_ids
    except KeyError:
        write_messages(user_id, 'Ошибка получения токена')
#
# print(get_photos_id(722061506))

def get_gender(user_id):
    '''Получить пол пользователя и сменить на противоположный'''
    url = f'https://api.vk.com/method/users.get'
    parameters = {'access_token': access_token,
                  'user_ids': user_id,
                  'fields': 'sex',
                  'v': 5.131
                  }
    result = requests.get(url, params=parameters)
    response = result.json()
    try:
        info_from_dict = response['response']
        for i in info_from_dict:
            sex = i.get('sex')
            if sex == 1:
                return 'woman'
            elif sex == 2:
                return 'man'
            else:
                return 'This is not Thailand!'

    except KeyError:
        write_messages(user_id, 'Receiving token error, please re-enter the token.')
#
# print(get_gender(722061506))

def min_permission_age(user_id):
    '''ПОЛУЧИТЬ МИНИМАЛЬНО-ВОЗМОЖНЫЙ ВОЗРАСТ, ДАБЫ НЕ ПРИСЕСТЬ НА ВОСЬМЕРКУ'''
    url = f'https://api.vk.com/method/users.get'
    params = {'access_token': access_token,
              'user_ids': user_id,
              'fields': 'bdate',
              'v': 5.131
              }
    result = requests.get(url, params=params)
    responce = result.json()
    try:
        info_from_response = responce['response']
        for elem in info_from_response:
            date = elem['bdate']
            bdate_list = elem['bdate'].split('.')
            if len(bdate_list) == 3:
                bdate = int(bdate_list[2])
                current_year = datetime.date.today().year
                return current_year - bdate
            elif date not in info_from_response:
                write_messages(user_id, 'Entering the minimum possible age, but no smaller than 18: ')
                for event in long_pool.listen():#не работает long_pool, разобраться
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                        age = event.text
                        return age
    except KeyError:
        write_messages(user_id, 'Receiving token error, please re-enter the token.')

#
def cities(user_id, city_name):
    """ПОЛУЧЕНИЕ ID ГОРОДА ПОЛЬЗОВАТЕЛЯ ПО НАЗВАНИЮ"""
    url = f'https://api.vk.com/method/database.getCities'
    params = {'access_token': access_token,
              'country_id': 1,
              'q': f'{city_name}',
              'need_all': 0,
              'count': 1000,
              'v': '5.131'}
    repl = requests.get(url, params=params)
    response = repl.json()
    try:
        information_list = response['response']
        list_cities = information_list['items']
        for i in list_cities:
            found_city_name = i.get('title')
            if found_city_name == city_name:
                found_city_id = i.get('id')
                return int(found_city_id)
    except KeyError:
        write_messages(user_id, 'Ошибка получения токена')
# print(cities(722061506, 'Вологда'))
#
# def find_city(user_id):
#     """ПОЛУЧЕНИЕ ИНФОРМАЦИИ О ГОРОДЕ ПОЛЬЗОВАТЕЛЯ"""
#     url = f'https://api.vk.com/method/users.get'
#     params = {'access_token': access_token,
#               'fields': 'city',
#               'user_ids': user_id,
#               'v': '5.131'}
#     repl = requests.get(url, params=params)
#     response = repl.json()
#     try:
#         information_dict = response['response']
#         for i in information_dict:
#             if 'city' in i:
#                 city = i.get('city')
#                 id = str(city.get('id'))
#                 return id
#             elif 'city' not in i:
#                 write_messages(user_id, 'Введите название вашего города: ')
#                 for event in long_pool.listen():
#                     if event.type == VkEventType.MESSAGE_NEW and event.to_me:
#                         city_name = event.text
#                         id_city = cities(user_id, city_name)
#                         if id_city != '' or id_city != None:
#                             return str(id_city)
#                         else:
#                             break
#     except KeyError:
#         write_messages(user_id, 'Ошибка получения токена')
#
#
# def find_user(user_id):
#     """ПОИСК ЧЕЛОВЕКА ПО ПОЛУЧЕННЫМ ДАННЫМ"""
#     url = f'https://api.vk.com/method/users.search'
#     params = {'access_token': access_token,
#               'v': '5.131',
#               'sex': get_gender(user_id),
#               'age_from': min_permission_age(),
#               # 'age_to': get_age_high(user_id),
#               'city': find_city(user_id),
#               'fields': 'is_closed, id, first_name, last_name',
#               'status': '1' or '6',
#               'count': 500}
#     resp = requests.get(url, params=params)
#     resp_json = resp.json()
#     try:
#         dict_1 = resp_json['response']
#         list_1 = dict_1['items']
#         for person_dict in list_1:
#             if person_dict.get('is_closed') == False:
#                 first_name = person_dict.get('first_name')
#                 last_name = person_dict.get('last_name')
#                 vk_id = str(person_dict.get('id'))
#                 vk_link = 'vk.com/id' + str(person_dict.get('id'))
#                 insert_data_users(first_name, last_name, vk_id, vk_link)
#             else:
#                 continue
#         return f'Поиск завершён'
#     except KeyError:
#         write_messages(user_id, 'Ошибка получения токена')
#
#

# def get_photo_1(user_id):
#     """ПОЛУЧЕНИЕ ID ФОТОГРАФИИ № 1"""
#     list = get_photos_id(user_id)
#     count = 0
#     for i in list:
#         count += 1
#         if count == 1:
#             return i[1]
#
#
# def get_photo_2(user_id):
#     """ПОЛУЧЕНИЕ ID ФОТОГРАФИИ № 2"""
#     list = get_photos_id(user_id)
#     count = 0
#     for i in list:
#         count += 1
#         if count == 2:
#             return i[1]
#
#
# def get_photo_3(user_id):
#     """ПОЛУЧЕНИЕ ID ФОТОГРАФИИ № 3"""
#     list = get_photos_id(user_id)
#     count = 0
#     for i in list:
#         count += 1
#         if count == 3:
#             return i[1]
#
#
# def send_photo_1(user_id, message, offset):
#     """ОТПРАВКА ПЕРВОЙ ФОТОГРАФИИ"""
#     session.method('messages.send', {'user_id': user_id,
#                                      'access_token': access_token,
#                                      'message': message,
#                                      'attachment': f'photo{person_id(offset)}_{get_photo_1(person_id(offset))}',
#                                      'random_id': 0})
#
#
# def send_photo_2(user_id, message, offset):
#     """ОТПРАВКА ВТОРОЙ ФОТОГРАФИИ"""
#     session.method('messages.send', {'user_id': user_id,
#                                      'access_token': access_token,
#                                      'message': message,
#                                      'attachment': f'photo{person_id(offset)}_{get_photo_2(person_id(offset))}',
#                                      'random_id': 0})
#
#
# def send_photo_3(self, user_id, message, offset):
#     """ОТПРАВКА ТРЕТЬЕЙ ФОТОГРАФИИ"""
#     session.method('messages.send', {'user_id': user_id,
#                                      'access_token': access_token,
#                                      'message': message,
#                                      'attachment': f'photo{person_id(offset)}_{get_photo_3(person_id(offset))}',
#                                      'random_id': 0})
#
#
# def find_persons(self, user_id, offset):
#     write_messages(user_id, found_person_info(offset))
#     person_id(offset)
#     insert_data_seen_users(person_id(offset), offset)  # offset
#     get_photos_id(person_id(offset))
#     send_photo_1(user_id, 'Фото номер 1', offset)
#     if get_photo_2(person_id(offset)) != None:
#         send_photo_2(user_id, 'Фото номер 2', offset)
#         send_photo_3(user_id, 'Фото номер 3', offset)
#     else:
#         write_messages(user_id, f'Больше фотографий нет')
#
#
# def found_person_info(self, offset):
#     """ВЫВОД ИНФОРМАЦИИ О НАЙДЕННОМ ПОЛЬЗОВАТЕЛИ"""
#     tuple_person = select(offset)
#     list_person = []
#     for i in tuple_person:
#         list_person.append(i)
#     return f'{list_person[0]} {list_person[1]}, ссылка - {list_person[3]}'
#
#
# def person_id(self, offset):
#     """ВЫВОД ID НАЙДЕННОГО ПОЛЬЗОВАТЕЛЯ"""
#     tuple_person = select(offset)
#     list_person = []
#     for i in tuple_person:
#         list_person.append(i)
#     return str(list_person[2])
#
