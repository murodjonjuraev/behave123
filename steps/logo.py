import time

from behave import *
from selenium import webdriver


@given(u'User launch chrome browser')
def launch_browser(context):
    # context.driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")
    context.driver = webdriver.Chrome()
    time.sleep(3)


@when(u'open Automation Practice homepage')
def open_home_page(context):
    context.driver.get("http://automationpractice.com/")
    time.sleep(3)


@then(u'verify that the logo present on page')
def verify_logo(context):
    status = context.driver.find_element_by_xpath("//img[@class='logo img-responsive']").is_displayed()
    assert status
    time.sleep(3)


@then(u'close browser')
def close_browser(context):
    context.driver.close()
