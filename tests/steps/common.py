from behave import given
from tests.framework.selenium_driver import webapp


@given(u'I load the website')
def step_impl_load_website(context):
    webapp.goto_page()
