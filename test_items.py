import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_basket_to_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert bool(button) == True, "Отсутствует кнопка для добавления товара в корзину"
