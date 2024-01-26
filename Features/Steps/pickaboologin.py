from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@given('Lauch the Chrome')
def lunch(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('Open the Pickaboo Login Page')
def link(context):
    context.driver.get("https://www.pickaboo.com/login/")


@when('Enter Mobile Number "{user}" and Password "{pwd}"')
def user_and_password(context, user, pwd):
    mobile = context.driver.find_element(By.XPATH, "//input[@placeholder='Mobile Number/Email']")
    password = context.driver.find_element(By.XPATH, "//input[@placeholder='Password']")

    mobile.send_keys(user)
    password.send_keys(pwd)
    context.password = password


@when('Click on the login Button')
def click_button(context):
    # Click the login button by sending the Enter key
    context.password.send_keys(Keys.ENTER)


@then('User Must successfull login')
def login_information(context):
    # Wait for the next page to load
    try:
        c = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sub-items"))
        )
        text = c.find_element(By.TAG_NAME, "p")
        final_text = text.text
        if final_text == "My Account":
            print("Test Passed")

    except TimeoutException:
        print("Timed out waiting for the next page to load")

    # Close the browser window
    context.driver.close()
