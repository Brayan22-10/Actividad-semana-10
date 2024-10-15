from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.turnitin.com/login_page.asp?lang=en_us")

correo = driver.find_element(By.ID, "email")
correo.send_keys("kevin25")
time.sleep(5)

clave = driver.find_element(By.NAME, "user_password")
clave.send_keys("12345678910")
time.sleep(5)

boton = driver.find_element(By.CLASS_NAME, "submit")
boton.click()
time.sleep(7)

driver.quit()