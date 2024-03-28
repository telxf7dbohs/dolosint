from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.example.com")
element = driver.find_element_by_id("some-id")

element.click()
