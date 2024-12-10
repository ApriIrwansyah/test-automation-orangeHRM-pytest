# pytest tests/test_admin.py
# pytest tests/test_admin.py --html=reports/admin.html --self-contained-html
# pytest  tests/test_admin.py --junitxml=reports/admin.xml

from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_admin_search(driver: WebDriver):
    
    try:
        # Inisialisasi object halaman
        login_page = LoginPage(driver)
        admin_page = AdminPage(driver)
        
        # Proses masuk ke website
        login_page.navigate_url()
        
        # Proses login
        login_page.form_login("Admin", "admin123")
        
        # Proses menginput form admin
        admin_page.form_admin("Admin")
        admin_page.take_screenshot("valid_admin")
        # verifikasi jika berhasil
        # assert "(1) Records Found" ==  admin_page.recfound().text
    except:
        print("Test Case Valid Admin Failed")
        admin_page.take_screenshot("invalid_admin")
