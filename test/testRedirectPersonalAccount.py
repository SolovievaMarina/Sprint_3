class TestRedirectPersonalAccount:

    from selenium.webdriver.common.by import By
    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Проверить переход по клику на «Личный кабинет».

    #вводим email/пароль
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("marinasolovieva2777@yandex.ru")
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("123456")

    #нажимаем "Войти"
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

    #нажимаем "Личный кабинет"
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()

    # закрыть браузер
    driver.quit()



