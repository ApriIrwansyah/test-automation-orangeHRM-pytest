from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
#from datetime import datetime
import os
from time import sleep

SCREENSHOT_DIR = os.path.join(os.getcwd(), 'screenshot')  # Folder untuk screenshot

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard = (By.XPATH, "//h6[text()='Dashboard']")
        # (By.XPATH, "//h6[normalize-space()='Dashboard']")
    def take_screenshot(self,name):
        # Take screenshot
        screenshot_name = f"screenshot_{name}.png"
        screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_name)

        # Membuat Folder jika tidak ditemukan
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        self.driver.save_screenshot(screenshot_path)

        # Verifikasi screenshot di simpan
        assert os.path.exists(screenshot_path), f"Screenshot not saved at {screenshot_path}"
    
    def get_att_page(self):
       self.driver.find_element(*self.dashboard).text
       sleep(2)
        
        
        
        
        
        
        