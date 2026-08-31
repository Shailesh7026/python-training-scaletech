from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

drv = webdriver.Chrome()
drv.get("https://www.google.com//")


box = drv.find_element(By.NAME, "q")
box.send_keys("Python", Keys.RETURN)

# Wait and close browser
time.sleep(5)
drv.quit()