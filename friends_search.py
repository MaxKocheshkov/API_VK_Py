from urllib.parse import urlencode
import requests

# Task 1

user_1_id = input('Введите id пользователя 1: ')
user_2_id = input('Введите id пользователя 2: ')

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

class User():
    def __init__(self, token):
        self.token = token
    
    def ids(self, user_1_id, user_2_id):
        self.user_1_id = user_1_id
        self.user_2_id = user_2_id

    def get_user(self):
        user_info = requests.get(
            'https://api.vk.com/method/users.get',
            params={
                'access_token': self.token,
                'user_ids': self.user_id,
                'v': 5.103, 
                }
        )
        return user_info.json()

    def get_friends(self):
        user_friends = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': self.token,
                'user_id': self.user_id,
                'v': 5.103, 
                }
        )
        return user_friends.json()

# def mutual():
#     user1 = User(TOKEN)
#     user1.user_id = user_1_id 
#     for value_1 in user1.get_friends().values():
#         df_1 = value_1['items']

#     user2 = User(TOKEN)
#     user2.user_id = user_2_id   
#     for value_2 in user2.get_friends().values():
#         df_2 = value_2['items']

#     mutual_fr = []
#     for i in df_1:
#          for j in df_2:
#             if i == j:
#                 mutual_fr.append(i)
#                 break
#     return mutual_fr

# print(mutual())

# Task 2

def mutual_2():
    user1 = User(TOKEN)
    user1.user_id = user_1_id 
    for value_1 in user1.get_friends().values():
        df_1 = value_1['items']

    user2 = User(TOKEN)
    user2.user_id = user_2_id   
    for value_2 in user2.get_friends().values():
        df_2 = value_2['items']

    user_1 = set(df_1)
    user_2 = set(df_2)
    return user_1 & user_2

print(mutual_2())