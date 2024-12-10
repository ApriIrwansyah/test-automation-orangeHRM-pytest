from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os


class LoginPage:
    
    URL     = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    
    def __init__(self, driver):
        self.driver = driver
        # inputan 
        self.username   = (By.XPATH, "//input[@placeholder='Username']")
        self.password   = (By.XPATH, "//input[@placeholder='Password']")
        self.btn_login  = (By.XPATH, "//button[@type='submit']")
    
    def navigate_url(self):
        self.driver.get(self.URL)
        
    # def login(self, username, password):
    #     self.driver.find_element(*self.username).send_keys(username)
    #     self.driver.find_element(*self.password).send_keys(password)
    #     self.driver.find_element(*self.btn_login).click()
    
    
    def input_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)
        
    def input_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)
        
    def click_login(self):
        self.driver.find_element(*self.btn_login).click()
        
    def form_login(self, username, password):
        self.input_username(username)
        sleep(2)
        self.input_password(password)
        sleep(2)
        self.click_login()
        sleep(2)
    
        