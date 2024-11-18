import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()
# Теперь ваш драйвер готов к использованию
base_url = "https://www.saucedemo.com/"
driver.get(base_url)
driver.maximize_window()
login1 = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login1)
print("Input Login")

user_name.send_keys(Keys.BACKSPACE)
user_name.send_keys(Keys.BACKSPACE)
time.sleep(3)
user_name.send_keys("er")

password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By.XPATH, "//*[@id='login-button']")
button_login.click()
print("Click Button")


time.sleep(5)