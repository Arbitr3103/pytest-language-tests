import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

class TestFeedback:

    links = [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ]

    feedback_message = ""

    @pytest.fixture(scope="function")
    def browser(self):
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        yield browser
        print("\nquit browser..")
        browser.quit()

    @pytest.mark.parametrize("link", links)
    def test_check_feedback(self, browser, link):
        # Открываем страницу
        browser.get(link)

        # Авторизуемся (замените 'your_login' и 'your_password' на свой логин и пароль)
        login_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='login']"))
        )
        login_input.send_keys('bragin.arbitr@me.com')

        password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys('Egor2011!')

        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sign-form__btn"))
        )
        login_button.click()

        # Ожидаем, что текстовое поле для ответа будет видимым и пустым
        textarea = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea.textarea"))
        )
        assert textarea.get_attribute("value") == ""

        # Вводим правильный ответ
        answer = str(math.log(int(time.time())))
        textarea.send_keys(answer)

        # Нажимаем кнопку "Отправить"
        submit_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        submit_button.click()

        # Ожидаем фидбек о том, что ответ правильный
        feedback = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.smart-hints__hint"))
        )
        feedback_text = feedback.text

        # Проверяем, что текст фидбека совпадает с "Correct!"
        assert feedback_text == "Correct!"

        # Добавляем текст фидбека к общему сообщению
        self.feedback_message += feedback_text + " "

    def pytest_sessionfinish(self):
        # Выводим общее сообщение после прохождения всех тестов
        print(self.feedback_message)



