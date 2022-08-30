from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestRegistration:
    def setup(self):
        options = Options()
        options.add_argument("no-sandbox")
        options.add_argument("--window-size=800,600")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    # Проверка 1. Регистрация с валидными данными (имя, email, пароль)
    def test_registration_with_valid_data(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        # заполнить данные для регистрации
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("Марина")
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("marinasolovieva2911@yandex.ru")
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]").send_keys("123457")

        # нажать "Зарегистрироваться"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()

        # ожидаем появления кнопки "Войти"
        assert self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]")


    # Тест2. Проверка регистрации с невалидным коротким паролем

    def test_registration_with_incorrect_data(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        # заполнить данные для регистрации
        self.driver.find_element(By.XPATH,  "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("Марина")
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("marinasolovieva2778@yandex.ru")
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]").send_keys("123")

        # нажать "Зарегистрироваться"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()

        # ожидаем появления сообщения "Некорректный пароль"
        assert self.driver.find_element(By.XPATH, "//p[contains(text(),'Некорректный пароль')]")

    def teardown(self):
        print('CLOSE')
        self.driver.close()
        self.driver.quit()



