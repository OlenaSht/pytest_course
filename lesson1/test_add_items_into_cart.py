from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_add_item_in_the_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    text_before_in_item = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link'] > div[class='inventory_item_name']").text
    print(text_before_in_item)

    add_to_cart_button = driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()

    cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    cart.click()

    text_after_in_item = driver.find_element(By.CSS_SELECTOR,
                                              "a[id='item_4_title_link'] > div[class='inventory_item_name']").text
    assert text_before_in_item == text_after_in_item





