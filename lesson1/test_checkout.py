from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_checkout_valid_data():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_name = driver.find_element(By.XPATH, "//*[text()='Sauce Labs Bike Light']")
    item_name.click()

    add_to_cart_button = driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-bike-light"]')
    add_to_cart_button.click()

    cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    cart.click()

    checkout_button = driver.find_element(By.XPATH, '//*[@data-test="checkout"]')
    checkout_button.click()

    first_name_field = driver.find_element(By.XPATH, '//input[@data-test="firstName"]')
    first_name_field.send_keys("Testfirstname")

    last_name_field = driver.find_element(By.XPATH, '//input[@data-test="lastName"]')
    last_name_field.send_keys("Testlastname")

    postal_code_field = driver.find_element(By.XPATH, '//input[@data-test="postalCode"]')
    postal_code_field.send_keys("80202")

    continue_button = driver.find_element(By.XPATH, '//input[@data-test="continue"]')
    continue_button.click()

    url_step2_checkout = driver.current_url
    assert url_step2_checkout == 'https://www.saucedemo.com/checkout-step-two.html'
    # print(url_step2_checkout)

    finish_button = driver.find_element(By.XPATH, "//*[@id='finish']")
    finish_button.click()

    url_checkout_complete = driver.current_url
    assert url_checkout_complete == 'https://www.saucedemo.com/checkout-complete.html'
    # print(url_checkout_complete)

    text_after_checkout = driver.find_element(By.XPATH,
                                             "//*[text()='Thank you for your order!']").text
    assert text_after_checkout == "Thank you for your order!"
    # print(text_after_checkout)

    driver.quit()