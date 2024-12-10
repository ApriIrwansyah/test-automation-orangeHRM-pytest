 # Employee Management page object
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import os

screenshot_dir = os.path.join(os.getcwd(), 'screenshot') # Folder untuk screenshot

class EmployeePage:
    URL     = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    
    def __init__(self,driver):
        self.driver = driver
        self.menu_item = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
        self.employee_name = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
        self.btn_search = (By.XPATH, "//button[normalize-space()='Search']")
        
        # Add the employees new
        self.add_employee = (By.XPATH, "//button[normalize-space()='Add']")
        self.first_name = (By.XPATH, "//input[@placeholder='First Name']")
        self.mid_name = (By.XPATH, "//input[@placeholder='Middle Name']")
        self.last_name = (By.XPATH, "//input[@placeholder='Last Name']")
        self.employee_id = (By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
        self.btn_save = (By.XPATH, "//button[normalize-space()='Save']")
        
        self.success_add = (By.XPATH, "//a[normalize-space()='Personal Details']")
    
    
    def take_screenshot(self, name):
        # take screenshot
        screenshot_name     = f"screenshot_{name}.png"
        screenshot_path     = os.path.join(screenshot_dir, screenshot_name)
        # Membuat folder screenshot jika belum ada
        os.makedirs(screenshot_dir, exist_ok=True)
        self.driver.save_screenshot(screenshot_path)
        
        # Verifikasi screenshoot di simpan
        assert os.path.exists(screenshot_path), f"Screenshot tidak disimpan di {screenshot_path}"
    
    def navigate_url(self):
        self.driver.get(self.URL)
    
    def get_menu_PIM(self):
        self.driver.find_element(*self.menu_item).click()
    
    def input_employee_name(self, name):
        self.driver.find_element(*self.employee_name).send_keys(name)
        
    def click_button(self):
        self.driver.find_element(*self.btn_search).click()
        
    def form_search(self, name):
        self.input_employee_name(name)
        sleep(1)
        self.click_button()
        
    def employee_new(self, FisrtName, midName, lastName, employee_id):
        self.driver.find_element(*self.add_employee).click()
        sleep(1)
        self.driver.find_element(*self.first_name).send_keys(FisrtName)
        sleep(1)
        self.driver.find_element(*self.mid_name).send_keys(midName)
        sleep(1)
        self.driver.find_element(*self.last_name).send_keys(lastName)
        sleep(1)
        self.driver.find_element(*self.employee_id).clear()
        self.driver.find_element(*self.employee_id).send_keys(employee_id)
        sleep(1)
        self.driver.find_element(*self.btn_save).click()
        
        
    def employee_success_add(self):
        self.driver.find_element(*self.success_add).text
    
        