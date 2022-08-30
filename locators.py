
"""Локаторы главной страницы"""
    entrance_to_account_button = "//button[contains(text(),'Войти в аккаунт')]" #кнопка Войти в аккаунт на главной
    personal_account_button = "//p[contains(text(),'Личный Кабинет')]" #кнопка "Личный кабинет" на главной
    sauces_tab = "//span[contains(text(),'Соусы')]" #вкладка "Соусы" на главной
    bread_tab = "//span[contains(text(),'Булки')]" #вкладка "Булки" на главной
    fillings_tab = "//span[contains(text(),'Начинки')]" #вкладка "Начинки" на главной

"""Локаторы страницы логина"""
    login_field = "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]" #поле Логин на странице /login
    password_field = "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]" #поле Пароль на странице /login
    entrance_button = "//button[contains(text(),'Войти')]" #кнопка Войти на странице /login
    register_button = "//a[contains(text(),'Зарегистрироваться')]" #кнопка Зарегистрироваться на странице /login

"""Локаторы страницы аккаунт"""
    exit_button = "//button[contains(text(),'Выход')]" #кнопка Выход на странице /account/profile
    constructor_tab = "//p[contains(text(),'Конструктор')]" #вкладка "Конструктор" на странице /account/profile
    logo_tab = "//header/nav[1]/div[1]/a[1]/*[1]" #логотип Stellar Burgers на странице /account/profile

"""Локаторы страницы регистрации"""
    name_field = "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]" #поле Имя на странице /register
    password_field_page_register= "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]" #поле Пароль на странице /register
    register_button_page_register = "//button[contains(text(),'Зарегистрироваться')]" #кнопка Зарегистрироваться на странице /register
    message_incorrect_pass = "//p[contains(text(),'Некорректный пароль')]" #сообщение Некорректный пароль на странице /register

