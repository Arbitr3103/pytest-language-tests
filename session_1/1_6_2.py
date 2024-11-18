from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти ссылку с зашифрованным текстом
    found_link = browser.find_element(By.PARTIAL_LINK_TEXT, "224592")
    time.sleep(5)
    # Кликнуть по найденной ссылке
    found_link.click()

    # Дать странице время на загрузку
    time.sleep(1)

    # Заполнить форму
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Закрыть браузер после выполнения
    time.sleep(10)
    browser.quit()