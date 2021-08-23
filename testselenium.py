from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time




driver = webdriver.Firefox()

driver.get("https://altinity.com/")

driver.find_element_by_link_text("Blog").click()

time.sleep(10)




assert "ALTIBITY BLOG" in driver.page_source

driver.close()



