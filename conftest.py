import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.firefox.options
import time
from selenium.webdriver.common.by import By


def test_add_to_cart_button(browser):
    # Ссылка на тестовую страницу
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Задержка для визуального осмотра страницы
    time.sleep(10)  # Подождать 10 секунд

    # Проверяем наличие кнопки добавления в корзину
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(add_to_cart_button) > 0, "Button 'Add to basket' not found on the page"


def pytest_addoption(parser):
    """Добавление пользовательских опций в pytest."""
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Specify the language for tests")
    parser.addoption('--pause', action='store', default=0, type=int,
                     help="Specify the pause duration (in seconds) before closing the browser")


@pytest.fixture(scope="function")
def browser(request):
    """Фикстура для инициализации браузера с учетом параметров."""
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    pause_duration = request.config.getoption("pause")
    browser = None

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print(f"\nStart Chrome browser for test with language '{user_language}'...")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = selenium.webdriver.firefox.options.Options()
        options.set_preference("intl.accept_languages", user_language)
        print(f"\nStart Firefox browser for test with language '{user_language}'...")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be 'chrome' or 'firefox'")

    yield browser

    # Добавляем паузу перед закрытием браузера
    if pause_duration > 0:
        print(f"\nPause for {pause_duration} seconds before quitting the browser...")
        time.sleep(pause_duration)

    print("\nQuit browser...")
    browser.quit()





