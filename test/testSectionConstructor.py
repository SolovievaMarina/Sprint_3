from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestSectionConstructor:
    def setup(self):
        options = Options()
        options.add_argument("no-sandbox")
        options.add_argument("--window-size=800,600")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    # Проверка 1. Переход к разделу "Соусы"
    def test_switching_to_sauces_section(self):
        self.driver.get("https://stellarburgers.nomoreparties.site")

        # нажимаем "Войти в аккаунт"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()

        # вводим логин/пароль
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("marinasolovieva2777@yandex.ru")
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("123456")

        # нажимаем "Войти"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

        # переходим на вкладку Соусы
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()

        # ожидаем появления элемента "Соус фирменный"
        assert self.driver.find_element(By.XPATH, "//p[contains(text(),'Соус фирменный Space Sauce')]")


    # Проверка 2. Переход к разделу "Булки"

    def test_switching_to_bread_section(self):
        self.driver.get("https://stellarburgers.nomoreparties.site")

        # нажимаем "Войти в аккаунт"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()

        # вводим логин/пароль
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("marinasolovieva2777@yandex.ru")
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("123456")

        # нажимаем "Войти"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

        # переходим на вкладку Соусы (тк по умолчанию уже находимся на вкладке Булки)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()

        # переходим к разделу "Булки"
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Булки')]").click()

        # ожидаем появления элемента 'Флюоресцентная булка R2-D3'
        assert self.driver.find_element(By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]")


    # Проверка 3. Переход к разделу "Начинки"

    def test_switching_to_fillings_section(self):
        self.driver.get("https://stellarburgers.nomoreparties.site")

        # нажимаем "Войти в аккаунт"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()

        # вводим логин/пароль
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("marinasolovieva2777@yandex.ru")
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("123456")

        # нажимаем "Войти"
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

        # переходим к разделу "Начинки"
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Начинки')]").click()

        # ожидаем появления элемента 'Говяжий метеорит (отбивная)'
        assert self.driver.find_element(By.XPATH, "//p[contains(text(),'Говяжий метеорит (отбивная)')]")

    def teardown(self):
        print('CLOSE')
        self.driver.close()
        self.driver.quit()