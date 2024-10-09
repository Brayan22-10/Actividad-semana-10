from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://accounts.spotify.com/es/login?creation_point=https%3A%2F%2Fopen.spotify.com%2F%3Fsp_cid%3Dad32918967edabc82750a87821187071%26device%3Ddesktop&continue=https%3A%2F%2Fopen.spotify.com%2Fintl-es%3Fflow_ctx%3D489116ca-2de0-4aae-bd6a-1f7a21e43fb9%253A1728535259&flow_ctx=489116ca-2de0-4aae-bd6a-1f7a21e43fb9%3A1728535259")

correo = driver.find_element(By.ID, "login-username")
correo.send_keys("dfpachon")
time.sleep(5)

clave = driver.find_element(By.ID, "login-password")
clave.send_keys("12345678910")
time.sleep(5)

boton = driver.find_element(By.ID, "login-button")
boton.click()
time.sleep(7)

driver.quit()