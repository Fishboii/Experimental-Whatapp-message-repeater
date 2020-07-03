from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
while True:
        name = input("Name of recipient or group: ")
        msg = input("Message: ")
        nums = input("Number of messages: ")
        driver = webdriver.Chrome(executable_path=r'YOURPATHHERE')
        driver.get('https://web.whatsapp.com/')
        input('Hit ENTER after you scanned the QR code. \n')
        print("Bombs away")
        time.sleep(3)
        elem = driver.find_element_by_xpath("//span[@title='{}']".format(name)).click()
        elem = driver.find_element_by_xpath('//*[@data-tab="1"]')
        for i in range(int(nums)):
            elem.send_keys(msg)
            elem.send_keys(Keys.RETURN)
        print("     ,--.!,\n  __/   -*-\n,d08b.  '|`\n0088MM\n`9MMP'      ")
        print("Message(s) sent")
