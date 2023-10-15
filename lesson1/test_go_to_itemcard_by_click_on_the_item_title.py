from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_go_to_itemcard_through_the_title():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_title = driver.find_element(By.XPATH, "//*[text()='Sauce Labs Bike Light']")
    item_title.click()

    url_after = driver.current_url
    assert url_after == 'https://www.saucedemo.com/inventory-item.html?id=0'