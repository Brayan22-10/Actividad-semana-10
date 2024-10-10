from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.turnitin.com/login_page.asp?lang=en_us") 

username_xpath = "//input[@id='email']"
password_xpath = "//input[@id='password']"
login_button_xpath = "//body/div[1]/div[1]/form[1]/div[4]/div[2]/div[3]/input[1]"

driver.find_element(By.XPATH, username_xpath).send_keys("bsebastiancastillo@ucundinamarca.edu.co")

driver.find_element(By.XPATH, password_xpath).send_keys("Tatan1010")

driver.find_element(By.XPATH, login_button_xpath).click()

time.sleep(10)

driver.quit()
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.turnitin.com/login_page.asp?lang=en_us") 

username_xpath = "//input[@id='email']"
password_xpath = "//input[@id='password']"
login_button_xpath = "//body/div[1]/div[1]/form[1]/div[4]/div[2]/div[3]/input[1]"

driver.find_element(By.XPATH, username_xpath).send_keys("bsebastiancastillo@ucundinamarca.edu.co")

driver.find_element(By.XPATH, password_xpath).send_keys("Tatan1010")

driver.find_element(By.XPATH, login_button_xpath).click()

time.sleep(50)

driver.quit()