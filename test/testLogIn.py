from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestLogIn:
    def setup(self):
        options = Options()
        options.add_argument("no-sandbox")
        options.add_argument("--window-size=800,600")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    # Проверка 1. Вход по кнопке "Войти в аккаунт" на главной
    def test_login_button_on_main_page(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        # нажимаем "Войти в аккаунт"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()

        # вводим логин/пароль
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("marinasolovieva2777@yandex.ru")
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("123456")

        # нажимаем "Войти"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        self.driver.implicitly_wait(5)

        # Ожидаем появления кнопки "Оформить заказ"
        assert self.driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]")


    # Проверка 2. Вход через кнопку «Личный кабинет»
    def test_login_button_personal_account(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        # нажимаем "Личный кабинет"
        self.driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        self.driver.implicitly_wait(5)

        # вводим логин/пароль
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("marinasolovieva2777@yandex.ru")
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("123456")

        # нажимаем "Войти"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

        # Ожидаем появления кнопки "Оформить заказ"
        assert self.driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]")


    # Проверка 3. Вход через кнопку в форме регистрации
    def test_login_from_registration_form(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        # нажимаем "Войти"
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()

        # вводим email/пароль
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("marinasolovieva2777@yandex.ru")
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("123456")

        # нажимаем "Войти"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

        # Ожидаем появления кнопки "Оформить заказ"
        assert self.driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]")


    # Проверка 4. Вход через кнопку в форме восстановления пароля
    def test_login_from_forgot_password_form(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        # нажимаем "Войти"
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()

        # вводим email/пароль
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("marinasolovieva2777@yandex.ru")
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("123456")

        # нажимаем "Войти"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

        # Ожидаем появления кнопки "Оформить заказ"
        assert self.driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    def teardown(self):
        print('CLOSE')
        self.driver.close()
        self.driver.quit()
