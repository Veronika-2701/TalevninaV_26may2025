import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


@allure.epic("Алтайвита")
@allure.severity("blocker")
class Altaivita:
    """Этот класс представляет сущность сайта Алтайвита."""
    @allure.id("инициализация Алтайвита")
    def __init__(self, driver):
        """Эта функция инициализует драйвер"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 70)
        driver.set_page_load_timeout(20)

    @allure.id("Выбор категории")
    def category_but(self):
        """Эта функция создает цикл,
        который скролит страницу и ищет нужный элемент,
        до того пока не найдет, затем закрывается."""
        while True:
            try:
                self.category = self.driver.find_element(
                    By.CSS_SELECTOR, "#group_tag-bg-category_1"
                    )
                self.wait.until(EC.element_to_be_clickable(self.category))
                if self.category:
                    self.category.click()
                    break
            
            except NoSuchElementException:
                self.driver.find_element(
                    By.CSS_SELECTOR, "html"
                    ).send_keys(Keys.PAGE_DOWN)

    @allure.id("выбор товара")
    def choice_prod(self):
        """Эта функция создает цикл,
        который скролит страницу и ищет нужный элемент,
        до того пока не найдет, затем закрывается."""
        while True:
            try:
                self.choice_product = self.driver.find_element(
                By.XPATH, '//img[starts-with(@title,'
                '"МСМ (Метилсульфонилметан), 60 капсул ТМ NaturalSupp")]'
                )
                if self.choice_product:
                    self.choice_product.click()
                    break
            
            except NoSuchElementException:
                self.driver.find_element(
                    By.CSS_SELECTOR, "html"
                    ).send_keys(Keys.PAGE_DOWN)

    @allure.id("добавление товара в корзину")     
    def add_to_cart(self):
        """Эта функция находит элемент,
        затем нажимает на него"""
        self.but_cart = self.driver.find_element(
                By.CSS_SELECTOR, '.btn-result_confirm_scroll'
                )
        self.but_cart.click()

    @allure.id("изменения товара в корзине (увеличение)")     
    def raise_prod_to_cart(self):
        """Эта функция находит элемент,
        затем нажимает на него"""
        self.but_plus = self.driver.find_element(
            By.CSS_SELECTOR, ".product-card__more."
            "product-card__plus-minus_2_0.main-btn.blue"
            ).find_element(By.CSS_SELECTOR,".more.js-plus_2_0"
                           ).click()

    @allure.id("удаление товара из корзины")     
    def delete_cart(self):
        """Эта функция находит элемент,
        затем нажимает на него"""
        self.cart_but = self.driver.find_element(
                By.CSS_SELECTOR, '.header__basket-link.'
                'ga_link_to_cart.grid_container_mobile_menu.'
                'pdd_cart'
                ).click()
        self.del_but = self.driver.find_element(
                By.XPATH, "//div[@data-item-product-id='4131']//button"
                )
        self.del_but.click()
