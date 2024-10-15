from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://accounts.spotify.com/es/login?creation_point=https%3A%2F%2Fopen.spotify.com%2F%3Fsp_cid%3Dad32918967edabc82750a87821187071%26device%3Ddesktop&continue=https%3A%2F%2Fopen.spotify.com%2Fintl-es%3Fflow_ctx%3D489116ca-2de0-4aae-bd6a-1f7a21e43fb9%253A1728535259&flow_ctx=489116ca-2de0-4aae-bd6a-1f7a21e43fb9%3A1728535259")  

username_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#login-username")) 
)
username_element.send_keys("Tatan10")

password_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#login-password"))  
)
password_element.send_keys("10tatan")

login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "body.encore-dark-theme.encore-layout-themes:nth-child(2) div.sc-cDelgQ.ealYxH.encore-dark-theme.encore-layout-themes:nth-child(7) div.sc-esHPOb.sc-fsKlOa.bCSeqD.fFJVRD:nth-child(1) div.sc-hNGPaV.hNTfFP div.sc-gJhJTp.sc-fQpRED.jIWbvU.jTGUSl div.Group-sc-u9bcx5-0.dTRcop.sc-epPVmt.gcMohz div.sc-gutikT.sc-huvEkS.fVbbtc.leTZEG button.Button-sc-qlcn5g-0.hFRjpO.encore-text-body-medium-bold span.ButtonInner-sc-14ud5tc-0.hvvTXU.encore-bright-accent-set > span.encore-text.encore-text-body-medium-bold.sc-iKTcqh.sc-gnpbhQ.doOTMr.cyUyia"))
)
login_button.click()

WebDriverWait(driver, 5).until(EC.url_changes("https://accounts.spotify.com/es/login?creation_point=https%3A%2F%2Fopen.spotify.com%2F%3Fsp_cid%3Dad32918967edabc82750a87821187071%26device%3Ddesktop&continue=https%3A%2F%2Fopen.spotify.com%2Fintl-es%3Fflow_ctx%3D489116ca-2de0-4aae-bd6a-1f7a21e43fb9%253A1728535259&flow_ctx=489116ca-2de0-4aae-bd6a-1f7a21e43fb9%3A1728535259"))

driver.quit()