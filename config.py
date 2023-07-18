user_token = ''  # токен пользователя
access_token = 'vk1.a.JnXakvfPOHM3QQY2n36a76hcdi1AT1x8UhdaesRFUnGg8JfDOhFDzjsRfqY17Lm-WnEoq-FuvN3zttOw1pBGo6Hr4RrfVpu6v2ZqR6AXRd6buTuXL6fqt54dpm2zhIvv4fJliVZRA1_RH0Pit75vh4wP0mYMencFKTL8XL41KlqsvL3j95jqoLO7kJ1r0M7FdQ5RwtRggI7wCjzk0wXhuw'
bot_key = 'iRJ19lhKFloxEH3RS7rs'
# service_key_access = '1b1f81ca1b1f81ca1b1f81caec180b563d11b1f1b1f81ca7fb869370890bfe2f63e8eec'

offset = 0  # сдвиг
line = range(0, 1000)  # последовательность для перебора найденных пользователей
host = '127.0.0.1'
user = 'postgres'
password = '0000'
db_name = 'bot_users'
link_get_token = 'https://oauth.vk.com/authorize?client_id=51697655&display=page&redirect_uri=https://vk.com/away.php?to=https://oauth.vk.com/blank.html&scope=248661618204893321077691124073410420050228075398673858720231988446579748506266688011743&response_type=token&v=5.131&state=123456'

'''ПОЛУЧИТЬ БИТОВУЮ МАСКУ'''
# notify	=   (1 << 0)	#Пользователь разрешил отправлять ему уведомления (для flash/iframe-приложений).
# friends	=   (1 << 1)#	Доступ к друзьям.
# photos	=   (1 << 2)	#Доступ к фотографиям.
# audio	=  (1 << 3)#	Доступ к аудиозаписям.
# video	=   (1 << 4)	#Доступ к видеозаписям.
# # stories	=  (1 << 6)	#Доступ к историям.
# # pages	=   (1 << 7)	#Доступ к wiki-страницам.
# # menu	=   (1 << 8)	#Добавление ссылки на приложение в меню слева.
# status	=   (1 << 10)#Доступ к статусу пользователя.
# # notes	=   (1 << 11)	#Доступ к заметкам пользователя.
# # messages	=  (1 << 12)	#Доступ к расширенным методам работы с сообщениями (только для Standalone-приложений, прошедших модерацию).
# offline	=  (1 << 16)#	Доступ к API в любое время (при использовании этой опции параметр expires_in, возвращаемый вместе с access_token, содержит 0 — токен бессрочный). Не применяется в Open API.
# # docs	=   (1 << 17)	#Доступ к документам.
# #
#
# # phone_number	=  (1 << 287)
# print(notify| photos|status|offline)
# # print(65536 & (1 << 2))
