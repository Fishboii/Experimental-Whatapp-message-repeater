from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
while True:
    try:
        name = input("Name of recipient or group: ")
        msg = input("Message: ")
        nums = input("Number of messages: ")
        driver = webdriver.Chrome(executable_path=r'C:\Users\junta\Desktop\Selenium drivers\Chromedriver.exe')
        driver.get('https://web.whatsapp.com/')
        input('Hit ENTER after you scanned the QR code.')
        time.sleep(3)
        elem = driver.find_element_by_xpath("//span[@title='{}']".format(name)).click()
        elem = driver.find_element_by_css_selector("._2S1VP.copyable-text.selectable-text")
        for i in range(int(nums)):
            elem.send_keys(msg)
            elem.send_keys(Keys.RETURN)
        print("Message has been sent")
    except:
        print('An error has occurred')
