from selenium import webdriver
from selenium.webdriver.common.by import By

def test_mark_attendance():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/attendance")
    driver.find_element(By.ID, "student-101").click()
    driver.find_element(By.ID, "submitBtn").click()
    msg = driver.find_element(By.ID, "status").text
    assert "Attendance Saved" in msg
    driver.quit()
    print("Attendance test PASSED")

if __name__ == "__main__":
    test_mark_attendance()
