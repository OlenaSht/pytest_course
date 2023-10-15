from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_about_button():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu_button = driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']")
    burger_menu_button.click()

    time.sleep(3)

    about_button = driver.find_element(By.CSS_SELECTOR, "a[id='about_sidebar_link']")
    about_button.click()

    url_after_about = driver.current_url
    assert url_after_about == 'https://saucelabs.com/'

    driver.quit()