from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_del_item_from_cart_through_itemcard():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_name = driver.find_element(By.XPATH, "//*[text()='Sauce Labs Bike Light']")
    item_name.click()

    text_before_in_cart = driver.find_element(By.XPATH,
                                              "//*[text()='Add to cart']").text

    add_to_cart_button = driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-bike-light"]')
    add_to_cart_button.click()

    text_in_button_after_adding_item =  driver.find_element(By.XPATH,
                                              "//*[text()='Remove']").text

    remove_to_cart_button = driver.find_element(By.XPATH, '//*[@data-test="remove-sauce-labs-bike-light"]')
    remove_to_cart_button.click()

    text_after_in_cart = driver.find_element(By.XPATH,
                                              "//*[text()='Add to cart']").text

    assert text_before_in_cart == text_after_in_cart
    assert text_in_button_after_adding_item == 'Remove'

    driver.quit()