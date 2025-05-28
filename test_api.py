import pytest
import allure
import json
from page.api import AltaiVita

ratata = AltaiVita("https://altaivita.ru/engine/")


@pytest.fixture()
@allure.title("Добавление в корзину товара")
@allure.description("Вызывает функцию,"
    "в которой валидный Request на методе Post.")
@allure.feature("Добавление в корзину товара")
@allure.severity("critical")
def test_add_to_cart():
    with allure.step("Request"):
        PROJ_RESP = ratata.req_post(
            'ajax/ajax_ecommerce/ajax_ecommerce.php',
            "action=ecom_link_products_cart&productID=7052&LANG_key=ru"
            "&S_wh=1&S_CID=f6912a102f7adf01682abe20f5e89554&S_cur_code=rub"
            "&S_koef=1&S_hint_code=&S_customerID="
            )
    with allure.step("Сравниваем, что в ответе код 200"):
        assert PROJ_RESP.status_code == 200
    with allure.step(
        "Сравниваем, что в теле ответа есть нужный id"
            ):
        js = json.loads(PROJ_RESP.text)
        tr = js["id"]
        assert tr == "7052"

@allure.title("Изменение количества товара в корзине (увеличение)")
@allure.description("Вызывает функцию,"
    "в которой валидный Request на методе Post.")
@allure.feature("Изменение количества товара в корзине (увеличение)")
@allure.severity("critical")
def test_raise_to_cart():
    with allure.step("Request"):
        PROJ_RESP = ratata.req_post(
            'cart/add_products_to_cart_from_preview.php',
            "product_id=7052&LANG_key=ru&S_wh=1&S_CID="
            "ee5cf64c887cba0964de2f597c66ae84&S_cur_code=rub"
            "&S_koef=1&quantity=1&S_hint_code=&S_customerID="
            )
    with allure.step("Сравниваем, что в ответе код 200"):
        assert PROJ_RESP.status_code == 200
    with allure.step(
        "Сравниваем, что в теле ответа есть сумма корзины"
            ):
        resp = PROJ_RESP.text
        name = "products_amount"
        assert name in resp

@allure.title("Удаление товара из корзины")
@allure.description("Вызывает функцию,"
    "в которой валидный Request на методе Post.")
@allure.feature("Удаление товара из корзины")
@allure.severity("critical")
def test_delete_to_cart():
    with allure.step("Request"):
        PROJ_RESP = ratata.req_post(
            'cart/add_products_to_cart_from_preview.php',
            "product_id=7052&LANG_key=ru&S_wh=1&S_CID="
            "ee5cf64c887cba0964de2f597c66ae84&S_cur_code"
            "=rub&S_koef=1&S_hint_code=&S_customerID="
            )
    with allure.step("Сравниваем, что в ответе код 200"):
        assert PROJ_RESP.status_code == 200
    with allure.step(
        "Сравниваем, что в теле ответа есть удаление прайса"
            ):
        resp = PROJ_RESP.text
        name = "price_to_delete"
        assert name in resp

@allure.title("Изменение количества товара в корзине (увеличение) с неправильным URL")
@allure.description("Вызывает функцию,"
    "в которой невалидный Request на методе Post.")
@allure.feature("Изменение количества товара в корзине (увеличение) с неправильным URL")
@allure.severity("critical")
def test_inval_1raise_to_cart():
    with allure.step("Request"):
        PROJ_RESP = ratata.req_post(
            'cart/add_products_to_cart_from_preview',
            "product_id=7052&LANG_key=ru&S_wh=1&S_CID="
            "ee5cf64c887cba0964de2f597c66ae84&S_cur_code=rub"
            "&S_koef=1&quantity=1&S_hint_code=&S_customerID="
            )
    with allure.step("Сравниваем, что в ответе код 404"):
        assert PROJ_RESP.status_code == 404

@allure.title("Изменение количества товара в корзине (увеличение) с неправильным body")
@allure.description("Вызывает функцию,"
    "в которой невалидный Request на методе Post.")
@allure.feature("Изменение количества товара в корзине (увеличение) с неправильным body")
@allure.severity("critical")
def test_inval_2raise_to_cart():
    with allure.step("Request"):
        PROJ_RESP = ratata.req_post(
            'cart/add_products_to_cart_from_preview.php',
            "product_id=&LANG_key=ru&S_wh=1&S_CID="
            "ee5cf64c887cba0964de2f597c66ae84&S_cur_code=rub"
            "&S_koef=1&quantity=1&S_hint_code=&S_customerID="
            )
    with allure.step(
        "Сравниваем, что в теле ответа есть error"
            ):
        js = json.loads(PROJ_RESP.text)
        tr = js["status"]
        assert tr == "error"