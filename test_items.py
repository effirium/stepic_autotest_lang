from selenium.webdriver.common.by import By
import pytest


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_exist(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    btn = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
	
    assert btn.text != "", f"Кнопки добавления в корзину нет"
