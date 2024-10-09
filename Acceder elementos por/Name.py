from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/?stype=lo&flo=1&deoia=1&jlou=AffNSz47QvZoxFwGiyckyOMgqKKhGmQzRvja9kZ-JeZ8Rxs6yaUe6uF_0LwDdWOz10famUy6yopr-ny-l62LiVBhfSPliYeK_yqLBMZIGvKElQ&smuh=30296&lh=Ac-3yWgMbe156GSb0XA")

correo = driver.find_element(By.NAME, "email")
correo.send_keys("3245168798")
time.sleep(5)

clave = driver.find_element(By.NAME, "pass")
clave.send_keys("clara10")
time.sleep(5)

boton = driver.find_element(By.NAME, "login")
boton.click()
time.sleep(50)

driver.quit()