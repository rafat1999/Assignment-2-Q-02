from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@given('Launch the Chrome Web Browser')
def Lunch(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('Go to the Login Page')
def login(context):
    context.driver.get("https://www.pickaboo.com/login/")


@then(u'Enter Mobile Number "{user}" and Password "{pwd}"')
def step_impl(context,user,pwd):
    mobile = context.driver.find_element(By.XPATH, "//input[@placeholder='Mobile Number/Email']")
    password = context.driver.find_element(By.XPATH, "//input[@placeholder='Password']")

    mobile.send_keys(user)
    password.send_keys(pwd)
    context.password = password


@then('Click on the login Button')
def login(context):
    # Click the login button by sending the Enter key
    context.password.send_keys(Keys.ENTER)


@then('go to the frist option on the smartphone list')
def f_phone(context):
    context.driver.get("https://www.pickaboo.com/product/infinix/")
    context.phones = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-one__single"))
    )


@then('Store the frist phones link in a list variable')
def s1_result(context):
    list_of_links = []

    # Find all 'h4' elements within the phones element
    e_l_1 = context.phones.find_elements(By.TAG_NAME, "h4")

    # Iterate over each 'h4' element
    for h4_element in e_l_1:
        # Find the 'a' element within each 'h4' element
        e_l = h4_element.find_elements(By.TAG_NAME, "a")

        # Iterate over each 'a' element
        for a_element in e_l:
            # Get the 'href' attribute value
            link = a_element.get_property('href')

            # Append the link to the list
            list_of_links.append(link)

    list_of_links


@then('go to the second option on the smartphone list')
def s_phone(context):
    context.driver.get("https://www.pickaboo.com/product/tecno/")
    context.phones = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-one__single"))
    )


@then('Store the second phones link in a list variable')
def s2_result(context):
    list_of_links_2 = []

    # Find all 'h4' elements within the phones element
    e_l_1 = context.phones.find_elements(By.TAG_NAME, "h4")

    # Iterate over each 'h4' element
    for h4_element in e_l_1:
        # Find the 'a' element within each 'h4' element
        e_l = h4_element.find_elements(By.TAG_NAME, "a")

        # Iterate over each 'a' element
        for a_element in e_l:
            # Get the 'href' attribute value
            link = a_element.get_property('href')

            # Append the link to the list
            list_of_links_2.append(link)

    list_of_links_2


@then(u'go to the third option on the smartphone list')
def t_phone(context):
    context.driver.get("https://www.pickaboo.com/product/realme/")
    context.phones = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-one__single"))
    )


@then(u'Store the third phones link in a list variable')
def s3_result(context):
    list_of_links_3 = []

    # Find all 'h4' elements within the phones element
    e_l_1 = context.phones.find_elements(By.TAG_NAME, "h4")

    # Iterate over each 'h4' element
    for h4_element in e_l_1:
        # Find the 'a' element within each 'h4' element
        e_l = h4_element.find_elements(By.TAG_NAME, "a")

        # Iterate over each 'a' element
        for a_element in e_l:
            # Get the 'href' attribute value
            link = a_element.get_property('href')

            # Append the link to the list
            list_of_links_3.append(link)

    list_of_links_3

@then('go to the foruth option on the smartphone list')
def f_phone(context):
    context.driver.get("https://www.pickaboo.com/product/oneplus/")
    context.phones = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-one__single"))
    )

@then('Store the fourth phones link in a list variable')
def s4_result(context):
    list_of_links_4 = []

    # Find all 'h4' elements within the phones element
    e_l_1 = context.phones.find_elements(By.TAG_NAME, "h4")

    # Iterate over each 'h4' element
    for h4_element in e_l_1:
        # Find the 'a' element within each 'h4' element
        e_l = h4_element.find_elements(By.TAG_NAME, "a")

        # Iterate over each 'a' element
        for a_element in e_l:
            # Get the 'href' attribute value
            link = a_element.get_property('href')

            # Append the link to the list
            list_of_links_4.append(link)

    list_of_links_4

@then('go to the fivth option on the smartphone list')
def fi_phone(context):
    context.driver.get("https://www.pickaboo.com/product/itel/")
    context.phones = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-one__single"))
    )

@then('Store the fivth phones link in a list variable')
def s5_result(context):
    list_of_links_5 = []

    # Find all 'h4' elements within the phones element
    e_l_1 = context.phones.find_elements(By.TAG_NAME, "h4")

    # Iterate over each 'h4' element
    for h4_element in e_l_1:
        # Find the 'a' element within each 'h4' element
        e_l = h4_element.find_elements(By.TAG_NAME, "a")

        # Iterate over each 'a' element
        for a_element in e_l:
            # Get the 'href' attribute value
            link = a_element.get_property('href')

            # Append the link to the list
            list_of_links_5.append(link)

    list_of_links_5

@then('go to the sixth option on the smartphone list')
def si_phone(context):
    context.driver.get("https://www.pickaboo.com/product/itel/")
    context.phones = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-one__single"))
    )

@then('Store the sixth phones link in a list variable')
def s6_result(context):
    list_of_links_6 = []

    # Find all 'h4' elements within the phones element
    e_l_1 = context.phones.find_elements(By.TAG_NAME, "h4")

    # Iterate over each 'h4' element
    for h4_element in e_l_1:
        # Find the 'a' element within each 'h4' element
        e_l = h4_element.find_elements(By.TAG_NAME, "a")

        # Iterate over each 'a' element
        for a_element in e_l:
            # Get the 'href' attribute value
            link = a_element.get_property('href')

            # Append the link to the list
            list_of_links_6.append(link)

    list_of_links_6

@then('go to the seventh option on the smartphone list')
def se_phone(context):
    context.driver.get("https://www.pickaboo.com/product/symphony/")
    context.phones = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-one__single"))
    )

@then('Store the Seventh phones link in a list variable')
def s7_result(context):
    list_of_links_7 = []

    # Find all 'h4' elements within the phones element
    e_l_1 = context.phones.find_elements(By.TAG_NAME, "h4")

    # Iterate over each 'h4' element
    for h4_element in e_l_1:
        # Find the 'a' element within each 'h4' element
        e_l = h4_element.find_elements(By.TAG_NAME, "a")

        # Iterate over each 'a' element
        for a_element in e_l:
            # Get the 'href' attribute value
            link = a_element.get_property('href')

            # Append the link to the list
            list_of_links_7.append(link)

    list_of_links_7

@then('go to the eigth option on the smartphone list')
def ei_phone(context):
    context.driver.get("https://www.pickaboo.com/product/benco/")
    context.phones = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-one__single"))
    )


@then('Store the Eigth phones link in a list variable')
def s8_result(context):
    list_of_links_8 = []

    # Find all 'h4' elements within the phones element
    e_l_1 = context.phones.find_elements(By.TAG_NAME, "h4")

    # Iterate over each 'h4' element
    for h4_element in e_l_1:
        # Find the 'a' element within each 'h4' element
        e_l = h4_element.find_elements(By.TAG_NAME, "a")

        # Iterate over each 'a' element
        for a_element in e_l:
            # Get the 'href' attribute value
            link = a_element.get_property('href')

            # Append the link to the list
            list_of_links_8.append(link)

    list_of_links_8

@then('go to the Ninth option on the smartphone list')
def ni_result(context):
    context.driver.get("https://www.pickaboo.com/product/iphone/")
    context.phones = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-one__single"))
    )


@then('Store the Ninth phones link in a list variable')
def s9_result(context):
    list_of_links_9 = []

    # Find all 'h4' elements within the phones element
    e_l_1 = context.phones.find_elements(By.TAG_NAME, "h4")

    # Iterate over each 'h4' element
    for h4_element in e_l_1:
        # Find the 'a' element within each 'h4' element
        e_l = h4_element.find_elements(By.TAG_NAME, "a")

        # Iterate over each 'a' element
        for a_element in e_l:
            # Get the 'href' attribute value
            link = a_element.get_property('href')

            # Append the link to the list
            list_of_links_9.append(link)

    list_of_links_9


@then('go to the tenth option on the smartphone list')
def t_phone(context):
    context.driver.get("https://www.pickaboo.com/product/xiaomi/")
    context.phones = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-one__single"))
    )

@then('Store the tenth phones link in a list variable')
def s10_result(context):
    list_of_links_10 = []

    # Find all 'h4' elements within the phones element
    e_l_1 = context.phones.find_elements(By.TAG_NAME, "h4")

    # Iterate over each 'h4' element
    for h4_element in e_l_1:
        # Find the 'a' element within each 'h4' element
        e_l = h4_element.find_elements(By.TAG_NAME, "a")

        # Iterate over each 'a' element
        for a_element in e_l:
            # Get the 'href' attribute value
            link = a_element.get_property('href')

            # Append the link to the list
            list_of_links_10.append(link)

    list_of_links_10