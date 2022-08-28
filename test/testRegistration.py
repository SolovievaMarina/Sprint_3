class TestRegistration:

    from selenium.webdriver.common.by import By
    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Тест1. Проверка регистрации с валидными данными (имя, email, пароль)

    #Ожидаем появления кнопки "Войти в аккаунт"
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")))

    #переход к регистрации
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()

    #заполнить данные для регистрации
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("Марина")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("marinasolovieva2678@yandex.ru")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]").send_keys("123457")

    #нажать "Зарегистрироваться"
    driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()

    #дождаться появления кнопки "Войти"
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]")))


    # Тест2. Проверка регистрации с невалидным паролем

    #переход к форме регистрации
    driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()

    #заполнить данные для регистрации с невалидным паролем (состоит из 3-цифр)
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("Марина")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("marinasolovieva260@yandex.ru")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]").send_keys("123")

    #нажать "Зарегистрироваться"
    driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()

    #дождаться появления сообщения "Некорректный пароль"
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Некорректный пароль')]")))

    #закрыть браузер
    driver.quit()



