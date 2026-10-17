from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")
    driver.find_element(By.ID, "username").send_keys("student01")
    driver.find_element(By.ID, "password").send_keys("pass123")
    driver.find_element(By.ID, "loginBtn").click()
    assert "Dashboard" in driver.title
    driver.quit()
    print("Login test PASSED")

if __name__ == "__main__":
    test_login()
