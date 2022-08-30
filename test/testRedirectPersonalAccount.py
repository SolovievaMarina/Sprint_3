from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestRedirectPersonalAccount:
    def setup(self):
        options = Options()
        options.add_argument("no-sandbox")
        options.add_argument("--window-size=800,600")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    # Проверка перехода по клику на «Личный кабинет».

    def test_redirect_by_click_on_button_personal_account(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        # вводим email/пароль
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("marinasolovieva2777@yandex.ru")
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("123456")

        # нажимаем "Войти"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

        # нажимаем "Личный кабинет"
        self.driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()

        # ожидаем текст в ЛК "В этом разделе вы можете изменить свои ПД"
        assert self.driver.find_element(By.XPATH, "//p[contains(text(),'В этом разделе вы можете изменить свои персональны')]")

    def teardown(self):
        print('CLOSE')
        self.driver.close()
        self.driver.quit()


