# Install report 
# pip install pytest pytest-html pytest-xdist

# pytest -s -v tests/test_login.py
# Perintah untuk laporan html ===========
# pytest -s -v tests/test_login.py --html=reports/report.html --self-contained-html
# perintah untuk laporan xml ============
# pytest -s -v tests/test_login.py --junitxml=reports/login.xml


from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from time import sleep
import pytest

import os
import sys

# sys.path.append('../') # Failed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_valid_login(driver: WebDriver):
    
    try :
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Inisialisasi objek halaman
        login_page      = LoginPage(driver)
        dashboard_page  = DashboardPage(driver)

        # Lakukan login
        login_page.form_login("Admin", "admin123")
            
        # Verifikasi berhasil masuk ke dashboard
        print(dashboard_page.get_att_page())
        dashboard_page.take_screenshot("valid_login")
    
    except:        
        # Verifikasi jika gagal login
        print("Test Case Valid Login Failed")
        dashboard_page.take_screenshot("invalid_login")