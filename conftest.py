import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: fr or other')


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

# import os
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# install_dir = "/snap/firefox/current/usr/lib/firefox"
# driver_loc = os.path.join(install_dir, "geckodriver")
# binary_loc = os.path.join(install_dir, "firefox")
# service = FirefoxService(driver_loc)
# opts = webdriver.FirefoxOptions()
# opts.binary_location = binary_loc
#
#
# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
# @pytest.fixture(scope='function')
# def browser(request):
#     browser = webdriver.Firefox(service=service, options=opts)
#     browser.implicitly_wait(5)
#     yield browser
#     browser.quit()

