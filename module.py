import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]


class Site:
    def __init__(self, address):
        if browser == "firefox":
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)
        elif browser == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(testdata["sleep_time"])
        self.driver.maximize_window()
        self.driver.get(address)

    def find_element(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property_element):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property_element)

    def registration(self, mode, user_log, user_passwd, user_btn, login, password):
        input1 = self.driver.find_element(mode, user_log)
        input1.send_keys(login)
        input2 = self.driver.find_element(mode, user_passwd)
        input2.send_keys(password)
        btn_clc = self.driver.find_element(mode, user_btn)
        btn_clc.click()

    def created_post(self, mode, created_btn, title_post, description_post, content_post, date_post,
                     btn_save_post, user_title, user_description, user_content, user_date):
        btn_crt = self.driver.find_element(mode, created_btn)
        btn_crt.click()
        title = self.driver.find_element(mode, title_post)
        title.send_keys(user_title)
        description = self.driver.find_element(mode, description_post)
        description.send_keys(user_description)
        content = self.driver.find_element(mode, content_post)
        content.send_keys(user_content)
        date = self.driver.find_element(mode, date_post)
        date.send_keys(user_date)
        btn_save = self.driver.find_element(mode, btn_save_post)
        btn_save.click()

    def close(self):
        self.driver.close()
