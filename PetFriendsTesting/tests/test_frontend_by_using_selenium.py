# pytest -v -s --driver Chrome --driver-path E:/chromedriver.exe
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle


@pytest.fixture(autouse=True)
def testing():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:

        # driver.implicitly_wait(10)
        # driver.get('http://petfriends.skillfactory.ru/login')
        # driver.find_element(By.ID, 'email').send_keys('alex__52@mail.ru')
        # driver.find_element(By.ID, 'pass').send_keys('123')
        # driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        # driver.find_element(By.XPATH, '//a[contains(text(), "Мои питомцы")]').click()
        # pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
        # yield driver
        # driver.quit()

        driver.implicitly_wait(5)
        driver.get('http://petfriends.skillfactory.ru/')

        for cookie in pickle.load(open("cookies.pkl", "rb")):
            driver.add_cookie(cookie)

        driver.refresh()
        driver.find_element(By.XPATH, '//a[contains(text(), "Мои питомцы")]').click()

    except Exception as ex:
        print(ex)

    yield driver
    driver.quit()


def test_show_my_pets(testing):
    driver = testing
    amount_my_pets_in_profile = int(
        driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split()[2])
    amount_my_pets_in_table = len(driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr'))
    assert amount_my_pets_in_profile == amount_my_pets_in_table
    print('\nКоличество питомцев в профиле', amount_my_pets_in_profile)
    print('Количество питомцев в таблице', amount_my_pets_in_table)


def test_pets_images(testing):
    driver = testing
    images = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/th/img')
    amount_img = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            amount_img += 1
    if amount_img >= len(images) / 2:
        print('\nУ пользователя хотя бы у половины питомцев есть фото питомцев')
    else:
        assert amount_img < len(images) / 2
        print('\nУ пользователя хотя бы у половины питомцев отсутствует фото питомцев')


def test_pets_info(testing):
    driver = testing
    names = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
    breed = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
    age = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')
    amount_names = 0
    amount_bread = 0
    amount_age = 0
    for i in range(len(names)):
        if names[i].get_attribute('textContent') == f"  ":
            amount_names += 1
        if breed[i].get_attribute('textContent') == f"  ":
            amount_bread += 1
        if age[i].get_attribute('textContent') == f"  ":
            amount_age += 1
    if amount_names == 0:
        print('\nУ всех питомцев есть имя')
    else:
        assert amount_names > 0
        print('\nУ некоторых питомцев отсутствует имя')
    if amount_bread == 0:
        print('\nУ всех питомцев есть порода')
    else:
        assert amount_bread > 0
        print('\nУ некоторых питомцев отсутствует порода')
    if amount_age == 0:
        print('\nУ всех питомцев есть возраст')
    else:
        assert amount_age > 0
        print('\nУ некоторых питомцев отсутствует возраст')


def test_pets_different_names(testing):
    driver = testing
    names = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
    amount_names = 0
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if names[i].get_attribute('textContent') == names[j].get_attribute('textContent'):
                amount_names += 1
    if amount_names == 0:
        print('\nУ всех питомцев разные имена')
    else:
        assert amount_names > 0
        print('\nПрисутствуют питомцы с одинаковыми именами')


def test_repeat_pets(testing):
    driver = testing
    names = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
    breed = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
    age = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')
    amount_pets = 0
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if (names[i].get_attribute('textContent') == names[j].get_attribute('textContent')
                    and breed[i].get_attribute('textContent') == breed[j].get_attribute('textContent')
                    and age[i].get_attribute('textContent') == age[j].get_attribute('textContent')):
                amount_pets += 1
    if amount_pets == 0:
        print('\nОтсутствуют повторяющиеся питомцы')
    else:
        assert amount_pets > 0
        print('\nПрисутствуют повторяющиеся питомцы')
