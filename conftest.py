import pytest
from selenium import webdriver
#from datetime import datetime
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Enter language. default "en"')
    parser.addoption('--browser', action='store', default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture(scope='function')
def browser(request):
    '''browser_name = request.config.getoption('browser')
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser_name
    print("\nquit browser..")
    ##now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    ##browser.save_screenshot('screenshot-%s.png' % now)
    browser.quit()'''
    language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language })
    print('\nstart browser...')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser...')
    browser.quit()