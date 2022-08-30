from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestLogOut:
    def setup(self):
        options = Options()
        options.add_argument("no-sandbox")
        options.add_argument("--window-size=800,600")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    # Проверка выхода по кнопке «Выйти» в личном кабинете
    def test_logout_button(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        # нажимаем "Войти в аккаунт"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()

        # вводим логин/пароль
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("marinasolovieva2777@yandex.ru")
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("123456")

        # нажимаем "Войти"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

        # нажимаем "Личный кабинет"
        self.driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()

        # нажимаем "Выход"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Выход')]").click()

        # ожидаем появления кнопки "Вход" на странице авторизации
        assert self.driver.find_element(By.XPATH, "//h2[contains(text(),'Вход')]")

    def teardown(self):
        print('CLOSE')
        self.driver.close()
        self.driver.quit()