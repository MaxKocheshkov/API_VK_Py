from urllib.parse import urlencode
import requests
import vk

# Task 3

user_id = input('Введите id пользователя 1: ')

APP_ID = 7406317
OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMS = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'user',
    'response_type': 'token',
    'v': '5.52'
}

"""
#Получение ссылки с токеном

print('?'.join(
    (OAUTH_URL, urlencode(OAUTH_PARAMS))
))

"""

TOKEN = 'dac755617697cfafa80e7109add6b56b3299aa773e7ff475c0b3eb2a021cbc34b6e3054d8a7ae14dd94bd'

session = vk.Session(access_token=TOKEN)
vk_api = vk.API(session)
for user_param in vk_api.users.get(user_id = user_id, fields = 'domain', v = 5.103):
    user_URL = 'https://vk.com/'+str(user_param['domain'])
    print(user_URL)