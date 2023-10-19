from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_filter_A_to_Z():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    filter_button = driver.find_element(By.CSS_SELECTOR, "[class='product_sort_container'] > option[value = 'hilo']")
    filter_button.click()

    item_name_1 = driver.find_element(By.XPATH, "(//div)[30]").text
    item_name_2 = driver.find_element(By.XPATH, "(//div)[70]").text

    # print(item_name_1, item_name_2)

    assert item_name_1 == '$49.99'
    assert item_name_2 == '$7.99'

    driver.quit()

