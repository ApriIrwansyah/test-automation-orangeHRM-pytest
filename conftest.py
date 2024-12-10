import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Setup WebDriver (Chrome sebagai contoh)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    yield driver  # Mengembalikan WebDriver ke test
    driver.quit()  # Teardown WebDriver setelah test selesai
