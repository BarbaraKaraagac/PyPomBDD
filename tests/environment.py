from tests.framework.selenium_driver import webapp
#import allure_behave.hooks


def after_feature(context, scenario):
    webapp.close_app()

#allure_report("/Users/basia/PycharmProjects/PyPomBDD/tests")