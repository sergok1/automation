from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YandexAutomate:

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path='./chromedriver')

    def login(self, email, password):
        self.browser.get('https://passport.yandex.ru/')

        self.browser.find_element_by_xpath('//*[@id="passp-field-login"]'
        ).send_keys(email)
        self.browser.find_element_by_xpath('//*[@id="passp:sign-in"]'
        ).click()
#very fast, need a pause to load
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="passp-field-passwd"]')
                )
            )
            
        self.browser.find_element_by_xpath('//*[@id="passp-field-passwd"]'
            ).send_keys(password)
        self.browser.find_element_by_xpath('//*[@id="passp:sign-in"]'
        ).click()



if __name__=='__main__':
                yandex = YandexAutomate()
                yandex.login('test.testov123456','Zxcvbnm,')


