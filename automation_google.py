from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://www.google.com/')
seearchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
seearchbox.send_keys('купить кофемашину bork c804')

seerchButton = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
seerchButton.click()

