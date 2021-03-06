from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.login_page import LoginPage
from tests.acceptance.page_model.register_page import RegisterPage
from tests.acceptance.page_model.add_algorithm_page import AddAlgorithmPage
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')


@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation_links
    matching_links = [l for l in links if l.text == link_text]
    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()


@when('I click on the Back to Home button')
def step_impl(context):
    page = BasePage(context.driver)
    page.back_to_home_button.click()


@when('I click on the dropdown menu')
def step_impl(context):
    page = BasePage(context.driver)
    page.dropdown_menu.click()


@when('I click on the "(.*)" dropdown link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.dropdown_links
    matching_links = [l for l in links if l.text == link_text]
    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = RegisterPage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('I enter "(.*)" in the "(.*)" login field')
def step_impl(context, content, field_name):
    page = LoginPage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('I choose "(.*)" field')
def step_impl(context, field_name):
    page = BasePage(context.driver)
    page.form_field(field_name).click()


@when('I press the submit button')
def step_impl(context):
    page = RegisterPage(context.driver)
    page.submit_button.click()


@when('I press the login button')
def step_impl(context):
    page = LoginPage(context.driver)
    page.submit_button.click()


@when('I choose a first answer')
def step_impl(context):
    page = HomePage(context.driver)
    page.form_fields[0].click()

@when('I press the Next button')
def step_impl(context):
    page = HomePage(context.driver)
    page.next_button.click()

@when('I press the Complete button')
def step_impl(context):
    page = HomePage(context.driver)
    page.complete_button.click()




@when('I type "(.*)" in "(.*)" field')
def step_impl(context, content, field_name):
    page = AddAlgorithmPage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('I press add algorithm button')
def step_impl(context):
    page = AddAlgorithmPage(context.driver)
    page.add_button.click()
