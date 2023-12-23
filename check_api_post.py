import requests
import yaml
import logging

with open('testdata.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# функция получения токена по логину и паролю
def get_login():
    path_1 = data.get('path_1')
    post = requests.post(url=path_1, data={'username': data.get('login'), 'password': data.get('password')})
    if post.status_code == 200:
        return post.json()['token']
    else:
        logging.error(f'Ошибка авторизации, код ошибки {post.status_code}. Проверьте пароль, логин. ')
        return None


# получение чужих постов по токену
def get_post_other(token):
    path_2 = data.get('path_2')
    get = requests.get(url=path_2, params={'owner': 'notMe'}, headers={'X-Auth-Token': token}) #получает чужие посты
    if get.status_code == 200:
        return get.json()
    else:
        logging.error(f'Kод ошибки {get.status_code}. Проверьте пароль, логин. ')
        return None

# получение своих постов по токену
def get_post_own(token):
    path_2 = data.get('path_2')
    get = requests.get(url=path_2, headers={'X-Auth-Token': token})
    if get.status_code == 200:
        return get.json()
    else:
        logging.error(f'Kод ошибки {get.status_code}. Проверьте пароль, логин. ')
        return None

# создание нового поста по токену
def create_post(token, title="Заголовок", description="Описание", content="контент"):
    username = data.get('login')
    password = data.get('password')
    path_2 = data.get('path_2')
    post = requests.post(url=path_2, headers={"X-Auth-Token": token}, params={
        'login': username,
        'password': password,
        'title': title,
        'description': description,
        'content': content})

    if post.status_code == 200:
        return post.json()['title']
    else:
        logging.error(f'Kод ошибки {post.status_code}. Проверьте пароль, логин. ')
        return None

