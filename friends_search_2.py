from urllib.parse import urlencode
import requests

# Task 2

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

TOKEN = '697dc83461d44467c5b4b62c43186652cc3250dfc94a6e8944fc7b40a9ce19efc2c2e47f53a2e405c94ca'

class User():
    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id
    
    # def ids(self, user_1_id, user_2_id):
    #     self.user_1_id = user_1_id
    #     self.user_2_id = user_2_id
    

    # def get_user(self):
    #     user_info = requests.get(
    #         'https://api.vk.com/method/users.get',
    #         params={
    #             'access_token': self.token,
    #             'user_ids': self.user_id,
    #             'v': 5.103, 
    #             }
    #     )
    #     return user_info.json()

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

    def __and__(self, other_user):
        self = User(TOKEN, user_1_id)
        other_user = User(TOKEN, user_2_id)
        for item in self.get_friends().values():
            other_user_fr = item.get('items')
        for item_1 in other_user.get_friends().values():
            other_user_fr_1 = item_1.get('items')
            mutal_user_list =  list(set(other_user_fr) & set(other_user_fr_1))
        return mutal_user_list
    

user1 = User(TOKEN, user_1_id)
user2 = User(TOKEN, user_2_id)
mutal_user_list = user1 & user2

def __str__():
        return f'список общих друзей пользователей {user_1_id} и {user_2_id}: \n {mutal_user_list} '
print(__str__())