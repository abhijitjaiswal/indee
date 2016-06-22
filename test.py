from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from utils import get_config_parser

class LoginTestCase(LiveServerTestCase):
    def setUp(self):
        # setUp is where you instantiate the selenium webdriver and loads the browser depending upon the config settings.
        self.config = get_config_parser("config.txt")
        if self.config.get("default", "browsertype") == "Chrome":
            self.selenium = webdriver.Chrome(self.config.get("default", "Chrome"))
        else:
            self.selenium = webdriver.Firefox()
       	
        self.selenium.maximize_window()
        super(LoginTestCase, self).setUp()

    def tearDown(self):
        # Call tearDown to close the web browser
        self.selenium.quit()
        super(LoginTestCase, self).tearDown()
        
    def test_user_login(self):
        #Load the URL
        self.selenium.get('https://preproduction.indee.tv/')
        
        #Find link to Login and Click on it
        Login = self.selenium.find_element_by_link_text('Login')
        self.assertEqual('Login', Login.text)
        Login.click()
        
        #Find Username field and key in username
        email = self.selenium.find_element_by_name('email')
        email.click()
        uname = "abhijit.jaiswal@gmail.com"
        email.send_keys(uname)
        
        #Find Password field and key in password
        password = self.selenium.find_element_by_name('password')
        password.click()
        password.send_keys("Indee77!@#")
        
        #Click Login button
        self.selenium.find_element_by_css_selector(".ind_bt[type='submit']").click()
        
        #Wait 10 seconds maximum for the home page to load and verify the username is same as used for login
        wait = WebDriverWait(self.selenium, 10)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.bt-menu")))
        element.click()
        lname = self.selenium.find_element_by_css_selector(".username").text
        self.assertEqual(lname, uname)