from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

USERNAME = 'admin'
PASSWORD = 'admin'

class User:
    def __init__(self):
     self.driver = webdriver.Chrome()

    def login(self):        
        self.driver.get("http://127.0.0.1:5500/user/index.html")

        sleep(60)

       # login_xpath =  self.driver.find_element_by_xpath('/html/body/form/input[3]')
        # login_xpath.click()
        login = self.driver.find_element('path', '/html/body/form/input[3]')

 

      


user = User()
user.login()