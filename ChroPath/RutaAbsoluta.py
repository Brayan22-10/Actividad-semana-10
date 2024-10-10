from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/?stype=lo&flo=1&deoia=1&jlou=AffNSz47QvZoxFwGiyckyOMgqKKhGmQzRvja9kZ-JeZ8Rxs6yaUe6uF_0LwDdWOz10famUy6yopr-ny-l62LiVBhfSPliYeK_yqLBMZIGvKElQ&smuh=30296&lh=Ac-3yWgMbe156GSb0XA")  

try:
    username_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]"))
    )
    username_element.send_keys("brayanlopez")

    password_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]"))
    )
    password_element.send_keys("tatn1010")

    login_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/button[1]"))
    )
    login_button.click()

    WebDriverWait(driver, 90).until(EC.url_changes("https://www.facebook.com/?stype=lo&flo=1&deoia=1&jlou=AffNSz47QvZoxFwGiyckyOMgqKKhGmQzRvja9kZ-JeZ8Rxs6yaUe6uF_0LwDdWOz10famUy6yopr-ny-l62LiVBhfSPliYeK_yqLBMZIGvKElQ&smuh=30296&lh=Ac-3yWgMbe156GSb0XA"))

finally:
    driver.quit() 