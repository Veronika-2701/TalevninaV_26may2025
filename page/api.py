import requests
import allure


@allure.epic("AltaiVita")
@allure.severity("blocker")
class AltaiVita:
    """Этот класс представляет сущность сайта AltaiVita."""
    @allure.id("инициализация сайта AltaiVita")
    def __init__(self, base_url) -> None:
        """Эта функция инициализирует base_url"""
        self.base_url = base_url       

    @allure.id("Request Post-запроса")
    def req_post(self, url="", text_data=""):
        """Эта функция создает оболочку Request Post-запроса"""
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;'
            'charset=UTF-8'}
        return requests.post(self.base_url + url,
                            headers=headers,
                            data=text_data)