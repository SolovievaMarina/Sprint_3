from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestRedirectFromPersonalAccountInConstructor:
    def setup(self):
        options = Options()
        options.add_argument("no-sandbox")
        options.add_argument("--window-size=800,600")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    # Проверка 1. Переход из ЛК в конструктор по клику на «Конструктор»

    def test_redirect_by_clicking_on_constructor(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        # вводим email/пароль
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("marinasolovieva2777@yandex.ru")
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("123456")

        # нажимаем "Войти"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

        # нажимаем "Личный кабинет"
        self.driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()

        # нажимаем "Конструктор"
        self.driver.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()

        # ожидаем появления кнопки "Оформить заказ" в конструкторе
        assert self.driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]")


    # Проверка 2. Переход из ЛК по клику на логотип Stellar Burgers.

    def test_redirect_by_clicking_on_logo(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        # вводим email/пароль
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("marinasolovieva2777@yandex.ru")
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("123456")

        # нажимаем "Войти"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

        # нажимаем "Личный кабинет"
        self.driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()

        # нажимаем на логотип Stellar Burgers
        self.driver.find_element(By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]").click()

        # ожидаем появления кнопки "Оформить заказ" в конструкторе
        assert self.driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    def teardown(self):
        print('CLOSE')
        self.driver.close()
        self.driver.quit()

