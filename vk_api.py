import requests

token = '3872f36d3872f36d3872f36d0d3800ae06338723872f36d66a4e813309e2bb997c65531'
version = '5.107'
user_id = input("Введите id пользователя, чьих друзей вы хотите увидеть" + '\n')
if user_id == '':
    user_id = '104011759'


def get_friends_by_id(id):
    response = requests.get('https://api.vk.com/method/friends.get', params={
        'access_token': token,
        'v': version,
        'user_id': id,
        'fields': 'nickname'
    })

    data = response.json()
    for i in data['response']['items']:
        print('{} {}'.format(i['first_name'], i['last_name']))


get_friends_by_id(user_id)
