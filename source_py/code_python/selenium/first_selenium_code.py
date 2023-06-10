import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver_path = "Users/ramon/Downloads/chromedriver_mac_arm64/chromedriver"
chrome_service = Service(driver_path)
driver = webdriver.Chrome(service=chrome_service)
#user_agent = driver.execute_script("return navigator.userAgent;")
site = "www.google.com.br"
driver.get(site)
print('ok')
driver.close()



