from behave import given, when, then

#an instance of the mainPage class
from tests.pages.main_page import mp

#an instance of the test_status class
from tests.utils.test_status import ts


@when(u'I search for "{phrase}"')
def step_impl ( context, phrase ):
    mp.search_phrase(phrase)
    mp.click_search_button()


@then(u'The result contains "{phrase}"')
def step_impl ( context, phrase ):
    result = mp.verify_search_result(phrase)
    ts.markFinal("TC: Duck Duck Go Searching", result, "The searching result is: " + str(result) + ".")

