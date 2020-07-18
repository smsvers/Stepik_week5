from time import sleep
from selenium.webdriver.common.by import By
from random import randint
link ='http://selenium1py.pythonanywhere.com'

def test_add_new_user(browser):
    browser.get(link)
    browser.find_element(By.ID, "login_link").click()
    browser.find_element(By.ID, "id_registration-email").send_keys(f"asdfasdf2-{randint(10,2000)}@mail.com")
    browser.find_element(By.ID, "id_registration-password1").send_keys("qwerreeree2342")
    browser.find_element(By.ID, "id_registration-password2").send_keys("qwerreeree2342")
    browser.find_element(By.NAME, "registration_submit").click()
    assert browser.find_element(By.CSS_SELECTOR, ".alertinner").text == "Thanks for registering!"
