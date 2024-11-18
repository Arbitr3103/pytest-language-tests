from selenium.webdriver.common.by import By


def test_add_to_cart_button(browser):
    # Ссылка на тестовую страницу
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Проверяем наличие кнопки добавления в корзину
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(add_to_cart_button) > 0, "Button 'Add to basket' not found on the page"
