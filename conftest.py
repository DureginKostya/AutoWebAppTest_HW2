import pytest
import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def login_xpath():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def password_xpath():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def button_xpath():
    return """//*[@id="login"]/div[3]/button"""


@pytest.fixture()
def result_xpath():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def result_login():
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def site_positive(login_xpath, password_xpath, button_xpath, result_login):
    my_site = Site(testdata["address"])
    my_site.registration('xpath',
                         login_xpath,
                         password_xpath,
                         button_xpath,
                         testdata['login'],
                         testdata['passwd'])
    yield my_site
    my_site.close()


@pytest.fixture()
def site_negative(login_xpath, password_xpath, button_xpath, result_xpath):
    my_site = Site(testdata["address"])
    my_site.registration('xpath',
                         login_xpath,
                         password_xpath,
                         button_xpath,
                         testdata['failed_login'],
                         testdata['failed_passwd'])
    yield my_site
    my_site.close()


@pytest.fixture()
def button_created():
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def new_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def new_description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def new_content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def new_date():
    return """//*[@id="create-item"]/div/div/div[5]/div/div/label/input"""


@pytest.fixture()
def button_save():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture()
def created_new_title():
    return """//*[@id="app"]/main/div/div[1]/h1"""
