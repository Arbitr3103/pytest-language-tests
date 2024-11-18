from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер
browser = webdriver.Chrome()

try:
    # Открываем страницу урока на Stepik
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)

    # Находим кнопку для входа и ожидаем ее видимости
    login_link = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#ember33"))
    )
    login_link.click()

    # Заполняем логин и пароль (замените 'your_login' и 'your_password' на свой логин и пароль)
    login_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#id_login_email"))
    )
    login_input.send_keys('bragin.arbitr@me.com')

    password_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#id_login_password"))
    )
    password_input.send_keys('Egor2011!')

    # Нажимаем Enter, чтобы авторизоваться
    password_input.send_keys(Keys.ENTER)

    # Ждем, пока не исчезнет поп-ап с авторизацией
    WebDriverWait(browser, 20).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "#login_form"))
    )



finally:
    # Закрываем браузер после всех действий
    browser.quit()




