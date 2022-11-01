import pytest
from api import Login

pf = Login()


def ids_login(val):
    return "login={0}".format(str(val))


def ids_password(val):
    return "password={0}".format(str(val))


def test_post_login_for_valid_login(login='login', password='password'):
    """ Проверяем какой статус возвращает запрос и что в результате содержится слово token"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.post_api_login(login, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'token' in result
    print('Response для login=login и password=password', result)


@pytest.mark.parametrize('login',
                         ['', 'log  in', ' login ', 'LOGIN', 'LoGiN', 'log,in.', 'login123', 'loгин',
                          '~`!@#$%^&*()_+<>?:”{}[];’'], ids=ids_login)
def test_post_login_for_no_valid_login(login, password='password'):
    """ Проверяем какой статус возвращает запрос и что в результате содержится слово token"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.post_api_login(login, password)

    # Сверяем полученные данные с нашими ожиданиями
    # Т.к валидации для полей нет, в ответе всегда приходит статус 200
    assert status == 200
    assert 'token' in result
    print('Response для login = {0}'.format(login))
    print(result)


@pytest.mark.parametrize('password',
                         ['', 'pass  word', ' pass ', 'PASS', 'PaSs', 'pas,s.', 'pass123', 'paсс',
                          '~`!@#$%^&*()_+<>?:”{}[];’'], ids=ids_password)
def test_post_login_for_no_valid_password(password, login='login'):
    """ Проверяем какой статус возвращает запрос и что в результате содержится слово token"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.post_api_login(login, password)

    # Сверяем полученные данные с нашими ожиданиями
    # Т.к валидации для полей нет, в ответе всегда приходит статус 200
    assert status == 200
    assert 'token' in result
    print('Response для password = {0}'.format(login))
    print(result)


def test_put_login_for_no_valid_method(login='login', password='password'):
    """ Проверяем какой статус возвращает put запрос"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, _ = pf.put_api_login(login, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 405
    print('Статус код для метода put', status)


def test_post_login_for_no_valid_content_type(login='login', password='password'):
    """ Проверяем какой статус возвращает put запрос"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, _ = pf.post_api_login_content_type(login, password)

    # Сверяем полученные данные с нашими ожиданиями
    # assert status == 415
    print('Статус код для метода put', status)
