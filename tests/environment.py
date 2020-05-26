from tests.framework.selenium_driver import webapp

def after_feature(context, scenario):
    webapp.close_app()

