from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_go_to_itemcard_through_the_picture():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_picture = driver.find_element(By.XPATH, "//*[@id='item_0_img_link']")
    item_picture.click()

    url_after = driver.current_url
    assert url_after == 'https://www.saucedemo.com/inventory-item.html?id=0'