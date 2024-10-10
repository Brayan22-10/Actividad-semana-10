from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/?stype=lo&flo=1&deoia=1&jlou=Afe7pCLsBEm1yeSu2xxxzT3fJ1MchTYMRayoChHnTt_CdZ5lUfgAxJzA3rEvI_1ppAPvFAB9VNdofeCSkPKvxEbW9RXbdR6I_Hw6ZKfqzQEWFA&smuh=30296&lh=Ac_A3arxwdWMl6lHwns")

link_recuperar = driver.find_element(By.PARTIAL_LINK_TEXT, "¿Olvidaste tu contraseña?")
link_recuperar.click()

time.sleep(5)

nombre = driver.find_element(By.ID, "identify_email")
nombre.send_keys("Brayan Castillo")

time.sleep(5)

boton = driver.find_element(By.NAME, "did_submit")
boton.click()

time.sleep(50)

driver.quit()
