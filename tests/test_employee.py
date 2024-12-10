from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from pages.login_page import LoginPage
from pages.employee_page import EmployeePage

# pytest tests/test_employee.py --html=reports/employee.html --self-contained-html
# pytest  tests/test_employee.py --junitxml=reports/employee.xml
# pytest -v -s tests/test_employee.py
def test_search_employee(driver: WebDriver):
    try:
        # Inisialisasi object halaman
        login_page      = LoginPage(driver)
        search_employee = EmployeePage(driver)
        
        login_page.navigate_url()
        search_employee.navigate_url()
        
        # Excekusi Object
        login_page.form_login("Admin", "admin123")
        
        # Exsekusi Object PIM
        search_employee.get_menu_PIM()
        search_employee.form_search('Amelia')

        # Verifikasi dengan screenshot jika berhasil 
        search_employee.take_screenshot('successfully added employee')
    except:
        # Verifikasi dengan screenshot jika berhasil 
        search_employee.take_screenshot('did not successfully added employee')
        
def test_employee_add(driver: WebDriver):
        # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    try:
        
        # Inisialisasi object halaman
        login_page      = LoginPage(driver)
        search_employee = EmployeePage(driver)
        
        login_page.navigate_url()
        search_employee.navigate_url()
        
        # Excekusi Object
        login_page.form_login("Admin", "admin123")
        
        # Exsekusi Object PIM
        search_employee.get_menu_PIM()
        search_employee.employee_new("Sisia", "lucia", "masia", "0010")
        
        # Success add employee
        # assert "Personal Details" in search_employee.employee_success_add()
        print(search_employee.employee_success_add())
        
        # Verifikasi dengan screenshot jika berhasil 
        search_employee.take_screenshot('successfully added employee')
    except:
        # Verifikasi dengan screenshot jika berhasil 
        search_employee.take_screenshot('did not successfully added employee')
    