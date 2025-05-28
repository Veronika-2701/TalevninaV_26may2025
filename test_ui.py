import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.ui import Altaivita
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture()
@allure.title("инициализация драйвера")
@allure.description(
    "Эта функция Инициализирует драйвер"
    "и открывает окно браузера на весь экран."
    "Затем получает URL, создает генератор,"
    "которые позволяют итерировать через последовательность данных,"
    "и закрывает браузер.")
@allure.feature("инициализация драйвера")
@allure.severity("blocker")
def driver():
    with allure.step("драйвер"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://altaivita.ru/")
        driver.set_page_load_timeout(10)
        driver.implicitly_wait(20)
        yield driver
        driver.quit()

@allure.title("Добавление товара в корзину через каталог")
@allure.description(
    "Вызывает функцию, вызывает класс, "
    "вызывает фунцию выбора каталога"
    "и выбора товара. Затем добавляет товар в корзину")
@allure.feature("Добавление товара в корзину через каталог")
@allure.severity("blocker")
def test_add_to_cart(driver):
    with allure.step("класс"):
        altavita = Altaivita(driver)
    with allure.step(
        "выбираем каталог, товар и добавляем"
        "товар в корзину"):
        altavita.category_but()
        altavita.choice_prod()
        altavita.add_to_cart()
        sleep(2)

    with allure.step("проверяем прайс корзины"):
        content = driver.find_element(By.CLASS_NAME, 
                                'basket-price.js-total').text
        assert content == "620 ₽"

@allure.title("Изменяем количество товара в корзине")
@allure.description(
    "Вызывает функцию, вызывает класс, "
    "вызывает фунцию выбора каталога"
    "и выбора товара. Затем добавляет товар в корзину"
    "и увеличивает количество на 1")
@allure.feature("Изменяем количество товара в корзине")
@allure.severity("blocker")
def test_raise_prod_to_cart(driver):
    with allure.step("класс"):
        altavita = Altaivita(driver)
    with allure.step(
        "выбираем каталог, товар и добавляем"
        "товар в корзину. Затем увеличиваем количество на 1"):
        altavita.category_but()
        altavita.choice_prod()
        altavita.add_to_cart()
        altavita.raise_prod_to_cart()
        sleep(2)

    with allure.step("проверяем прайс корзины"):
        content = driver.find_element(
            By.CLASS_NAME,
            'basket-price.js-total'
            ).text
        assert content == "1 240 ₽"

@allure.title("Удаление товара из корзины")
@allure.description(
    "Вызывает функцию, вызывает класс, "
    "вызывает фунцию выбора каталога"
    "и выбора товара. Затем добавляет"
    "товар в корзину, увеличивает количество"
    "на 1 и удаляет корзину")
@allure.feature("Удаление товара из корзины")
@allure.severity("blocker")
def test_delete_cart(driver):
    with allure.step("класс"):
        altavita = Altaivita(driver)
    with allure.step(
        "выбираем каталог, товар и добавляем"
        "товар в корзину. Затем увеличиваем "
        "количество на 1 и удаляет корзину"):
        altavita.category_but()
        altavita.choice_prod()
        altavita.add_to_cart()
        altavita.raise_prod_to_cart()
        altavita.delete_cart()
        sleep(2)

    with allure.step("проверяем прайс корзины"):
        content = driver.find_element(
            By.CLASS_NAME,
            'basket-price.js-total'
            ).text
        assert content == "0 ₽"


