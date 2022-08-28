class testSectionConstructor:

    from selenium.webdriver.common.by import By
    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    #ожидаем появления кнопки "Войти в аккаунт"
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")))

    #нажимаем "Войти в аккаунт"
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()

    #вводим логин/пароль
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("marinasolovieva2777@yandex.ru")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("123456")

    #нажимаем "Войти"
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

    # Ожидаем появления вкладки "Соусы"
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Соусы')]")))

    # Тест 1. Проверить переход к разделу "Соусы"
    driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()

    # Тест 2. Проверить переход к разделу "Булки"
    driver.find_element(By.XPATH, "//span[contains(text(),'Булки')]").click()

    # Тест 3. Проверить переход к разделу "Начинки"
    driver.find_element(By.XPATH, "//span[contains(text(),'Начинки')]").click()