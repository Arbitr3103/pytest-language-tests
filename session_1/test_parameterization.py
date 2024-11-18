import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


# Функция для получения текста фидбека
def get_feedback(browser):
    try:
        feedback = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        ).text
        return feedback
    except:
        return None


# Параметры теста - ссылки на задачи на Stepik
@pytest.mark.parametrize("link", [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_stepik_task(link):
    # Инициализируем переменную browser здесь
    browser = None

    try:
        # Открываем браузер
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)

        # Открываем страницу урока на Stepik
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

        # Вводим правильный ответ (поле перед вводом должно быть пустым)
        answer = math.log(int(time.time()))
        answer_input = WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".string-quiz__textarea"))
        )
        answer_input.send_keys(str(answer))

        # Нажимаем кнопку "Отправить"
        submit_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        submit_button.click()

        # Дожидаемся фидбека о том, что ответ правильный
        feedback = get_feedback(browser)
        assert feedback == "Correct!", f"Текст в опциональном фидбеке не совпадает: {feedback}"

    finally:
        # Закрываем браузер после всех действий
        browser.quit()





