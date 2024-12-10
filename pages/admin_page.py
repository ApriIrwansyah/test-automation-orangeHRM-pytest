from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import os
import pyautogui
from time import sleep

screenshot_dir = os.path.join(os.getcwd(), 'screenshot') # Folder untuk screenshot

class AdminPage:
    
    URL     = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    def __init__(self,driver):
        self.driver = driver
        self.driver.maximize_window()
        driver.implicitly_wait(10)
               
        self.menu_admins     = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")
        # Username
        self.username       = (By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
        # User Role
        self.role_input     = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/i[1]")        
        # Employee Name
        self.employee_name  = (By.XPATH, "//input[@placeholder='Type for hints...']")
        # Status
        self.status         = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]")
        # Btn Search
        self.btn_search     = (By.XPATH, "//button[normalize-space()='Search']")
        self.recfound       = (By.XPATH, "//span[normalize-space()='(1) Records Found']")
        
    # def form_admin(self, username, employee_name):
    #     # username
    #     self.driver.find_element(*self.username).send_keys(username)
    #     # rolr_user
    #     role = Select(self.driver.find_element(*self.role_input))
    #     role.select_by_visible_text('Admin')
    #     # employee_name
    #     self.driver.find_element(*self.employee_name).send_keys(employee_name)
    #     # status
    #     status = Select(self.driver.find_element(*self.input_status))
    #     status.select_by_visible_text("Enabled")
    
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
    
    def menu_admin(self):
        self.driver.find_element(*self.menu_admins).click()
    
    def input_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)
        
    def input_role(self):
        self.driver.find_element(*self.role_input).click()
        # role.select_by_visible_text("Admin")
        # pyautogui
        pyautogui.typewrite("Admin")
        pyautogui.press()
        
    
    def input_employee_name(self, employee_name):
        self.driver.find_element(*self.employee_name).send_keys(employee_name)
    
    def input_status(self):
        status = Select(self.driver.find_element(*self.input_status))
        status.select_by_visible_text("Enabled")
        pyautogui
        pyautogui.typewrite("Enabled")
        pyautogui.press()
        
    def btn_searchh(self):
        self.driver.find_element(*self.btn_search).click()
        
    def form_admin(self, username):
        self.menu_admin()
        self.input_username(username)
        sleep(1)
        self.btn_searchh()
        
    def get_att_success(self):
        self.driver.find_element(*self.recfound).text