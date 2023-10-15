from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_add_item_from_the_item_card():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    text_before_in_item = driver.find_element(By.CSS_SELECTOR, "a[id='item_0_title_link'] > div[class='inventory_item_name']").text
    print(text_before_in_item)

    item_name = driver.find_element(By.XPATH, "//*[text()='Sauce Labs Bike Light']")
    item_name.click()

    add_to_cart_button = driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-bike-light"]')
    add_to_cart_button.click()

    cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    cart.click()

    text_after_in_item = driver.find_element(By.CSS_SELECTOR,
                                               "a[id='item_0_title_link'] > div[class='inventory_item_name']").text
    assert text_before_in_item == text_after_in_item

    driver.quit()