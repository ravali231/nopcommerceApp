import pytest
from selenium import webdriver
from _pytest.compat import importlib_metadata
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching chrome browser")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

def pytest_addoption(parser): #will get the values from CLI/Hooks
    parser.addoption("--browser")

@pytest.fixture() #will return the browser value to setup method
def browser(request):
    return request.config.getoption("--browser")

######Pytest HTML reports#############
# Hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Ravali'

#It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)

#could not add data driven testing as ubuntu doesn't support xlx files.