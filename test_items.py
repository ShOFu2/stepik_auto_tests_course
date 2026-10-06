import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_cart_button(browser):
    browser.get(link)
    
    # Обязательная пауза (30 секунд) по условию задания для визуальной проверки через --language=fr
    time.sleep(30)
    
    # Ищем кнопку добавления товара в корзину по ее уникальному селектору на странице
    buttons = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button.btn-add-to-basket")
    
    # Проверяем с помощью assert, что кнопка присутствует на странице
    assert len(buttons) > 0, "Кнопка добавления в корзину не найдена на странице!"
