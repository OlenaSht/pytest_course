from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_delete_item_from_cart_in_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    add_to_cart_button = driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()

    cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    cart.click()

    # cart_badge_with_item = driver.find_element(By.XPATH, "a[class='shopping_cart_link']>span[class='shopping_cart_badge']").text

    remove_item = driver.find_element(By.XPATH, '//*[@data-test="remove-sauce-labs-backpack"]')
    remove_item.click()

    # cart_badge_without_item = driver.find_element(By.XPATH, "a[class='shopping_cart_link']>span[class='shopping_cart_badge']").text

    text_after_in_item = driver.find_element(By.CSS_SELECTOR, "div[class='cart_list'] > div[class='removed_cart_item']").text

    driver.quit()



