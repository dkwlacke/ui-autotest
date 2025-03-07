from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import unittest

class Test(unittest.TestCase):
   def test(self):
    link = "https://practice-automation.com/form-fields/"
    browser = webdriver.Chrome()
    browser.get(link)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    input1=browser.find_element(By.ID, "name-input")
    input1.send_keys("Maksim")
    input2 = browser.find_element(By.XPATH, "//input[@type='password']")
    input2.send_keys("qwerty")
    milk=browser.find_element(By.ID, "drink2")
    milk.click()
    time.sleep(5)
    coffe=browser.find_element(By.ID, "drink3")
    coffe.click()
    email=browser.find_element(By.ID, "email")
    email.send_keys("qwerty@gmail.com")
    select.select_by_visible_text("Yes")
    msg=browser.find_element(By.ID, "message")
    tool=browser.find_elements(By.XPATH, "//form/ul/li")
    dlina=str(len(tool))
    msg.send_keys(dlina)
    color=browser.find_element(By.ID, "color3")
    color.click()

    time.sleep(5)
    button = browser.find_element(By.ID, "submit-btn")
    button.click()
    time.sleep(20)

if __name__=="__main__":
    unittest.main()