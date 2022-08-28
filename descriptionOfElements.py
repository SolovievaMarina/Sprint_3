from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# 1. Локаторы для элементов главной страницы

# ожидаем появления кнопки "Войти в аккаунт" на главной странице
WebDriverWait(driver, 3).until(
    expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")))

# нажимаем "Войти в аккаунт" на главной странице
driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()

# ожидаем появления кнопки "Личный кабинет" на главной странице
WebDriverWait(driver, 3).until(
    expected_conditions.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Личный Кабинет')]")))

# нажимаем "Личный кабинет" на главной странице
driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()

# Ожидаем появления вкладки "Соусы" на главной странице
WebDriverWait(driver, 3).until(
    expected_conditions.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Соусы')]")))

# Тест 1. Переход к разделу "Соусы" на главной странице
driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()

# Тест 2. Переход к разделу "Булки" на главной странице
driver.find_element(By.XPATH, "//span[contains(text(),'Булки')]").click()

# Тест 3. Переход к разделу "Начинки" на главной странице
driver.find_element(By.XPATH, "//span[contains(text(),'Начинки')]").click()

# 2. Локаторы для элементов страницы /login

# вводим логин в форму авторизации на странице /login
driver.find_element(By.XPATH,
                    "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys(
    "marinasolovieva2777@yandex.ru")

# вводим пароль в форму авторизации на странице /login
driver.find_element(By.XPATH,
                    "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(
    "123456")

# нажимаем "Войти" на странице /login
driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

# переход к форме регистрации на странице /login
driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()

# дождаться появления кнопки "Войти" (в случае ввода валидного пароля в форме регистрации)
WebDriverWait(driver, 3).until(
    expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]")))

# 3. Локаторы для элементов страницы /account/profile

# ожидаем появления кнопки "Выход" на странице /account/profile
WebDriverWait(driver, 3).until(
    expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Выход')]")))

# нажимаем "Выход" на странице /account/profile
driver.find_element(By.XPATH, "//button[contains(text(),'Выход')]").click()

# нажимаем "Конструктор" на странице /account/profile
driver.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()

# нажимаем на логотип Stellar Burgers на странице /account/profile
driver.find_element(By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]").click()

# 4. Локаторы для элементов страницы /register

# заполнить валидным значением поле "имя" на странице /register
driver.find_element(By.XPATH,
                    "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys(
    "Марина")

# заполнить валидным значением поле "Email" на странице /register
driver.find_element(By.XPATH,
                    "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(
    "marinasolovieva260@yandex.ru")

# заполнить валидным значением поле "пароль" на странице /register
driver.find_element(By.XPATH,
                    "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]").send_keys(
    "123456")

# заполнить невалидным значением поле "пароль" (пароль из 3-х символов) на странице /register
driver.find_element(By.XPATH,
                    "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]").send_keys(
    "123")

# нажать "Зарегистрироваться" на странице /register
driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()

# дождаться появления сообщения "Некорректный пароль" (в случае ввода невалидного пароля) на странице /register
WebDriverWait(driver, 3).until(
    expected_conditions.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Некорректный пароль')]")))
