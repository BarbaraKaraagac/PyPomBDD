# PyPomBDD

This is an example of a python BDD framework with the usage of behave(Gherkin) and the page object model.

The feature is reatively simple - it's Duck Duck Go Searching with 2 scenarios (phrases).
The `phrase` value is passed from the feature itself.

  * Logging 
  
  The logging is quite detailed - after each tests run an automation.log file will be generated and you'll find an information about all the actions like locating elements, typing inputs etc there.
  
  * Screenshots
  
  Screenshots are taken in case of a failed test and saved in a tests/screenshots location.


# Requirements

view requirements:
  `cat requirements.txt`
  
install requirements:
  `pip install -r requirements.txt`
  
 # Run tests: 
 `behave tests/features`
 
 # Generate allure report (it will be an index.html file):
 
First run tests:
 
`behave -f allure_behave.formatter:AllureFormatter -o allure/results ./tests/features`

Then generate a report file (if you already have one generated and you want a new one, use '--clean' parameter):

`allure generate allure/results/ -o allure/reports`

In case of troubles with generating the report on Mac - please install allure via brew - 
`brew install allure`
in the command line.
 
 # Credits:
 
 Harsh Murari:
 https://github.com/Rhoynar/python-selenium-bdd.git
 
 Let's Kode It:
 https://www.udemy.com/course/selenium-webdriver-with-python3/
 
 Rahul Shetty:
 https://www.udemy.com/course/learn-selenium-automation-in-easy-python-language/
 
