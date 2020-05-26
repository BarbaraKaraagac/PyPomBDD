import tests.utils.custom_logger as cl
import logging
from tests.framework.selenium_driver import  webapp
from traceback import print_stack


class TestStatus():
    instance = None
    log = cl.customLogger(logging.DEBUG)

    @classmethod
    def get_instance ( cls ):
        if cls.instance is None:
            cls.instance = TestStatus()
        return cls.instance

    def __init__ ( self ):
        self.driver = webapp.get_driver()
        self.resultList=[]

    def setResult ( self, result, resultMessage ):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("The result of the test case is positive. " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("The result of the test case is negative. " + resultMessage)
                    webapp.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("The result of the test case is negative. " + resultMessage)
                webapp.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("An unexpected exception occured. ")
            webapp.screenShot(resultMessage)
            print_stack()

    def mark ( self, result, resultMessage ):

        self.setResult(result, resultMessage)

    def markFinal ( self, testName, result, resultMessage ):

        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + " TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True

ts = TestStatus.get_instance()
