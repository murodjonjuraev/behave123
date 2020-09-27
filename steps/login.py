import time

from behave import *
from selenium import webdriver

url = "http://automationpractice.com/"


@given('I launch Chrome browser')
def launching_browser(context):
    context.driver = webdriver.Chrome()
    time.sleep(3)


@when('I open Automation Practice home page')
def open_home_page(context):
    context.driver.get(url)
    time.sleep(3)


@when('I click on Sign in button')
def click_on_sign_in(context):
    context.driver.find_element_by_xpath("//div[@class='header_user_info']").click()
    time.sleep(3)


@when('Enter email address "{user}" and password "{pwd}"')
def enter_credentials(context, user, pwd):
    context.driver.find_element_by_id("email").send_keys(user)
    context.driver.find_element_by_id("passwd").send_keys(pwd)
    time.sleep(3)


@when('Click on login button')
def click_sign_in(context):
    context.driver.find_element_by_xpath("//p[@class='submit']//span[1]").click()


@then(u'User must successfully login to My account page')
def verify_my_account(context):
    text = context.driver.find_element_by_xpath("//span[@class='navigation_page']").text
    assert text == "My account"
    time.sleep(3)
    context.driver.close()
