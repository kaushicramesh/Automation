from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('/Applications/chromedriver')
# url = "https://itsmweb.cargill.com"
# driver.get(url)
# username = driver.find_element_by_id('username-id')
# username.send_keys('k685217')
# password = driver.find_element_by_id('pwd-id')
# password.send_keys('ImbeFruit11')
# driver.find_element_by_name('login').click()
# driver.implicitly_wait(10)
# val1 = driver.find_element_by_xpath('//*[@id="T301444200"]/tbody/tr[2]/td[1]/nobr/span')
# print(val1.text)
# val2 = driver.find_element_by_xpath('//*[@id="T301444200"]/tbody/tr[3]/td[1]/nobr/span')
# print(val2.text)
# val3 = driver.find_element_by_xpath('//*[@id="T301444200"]/tbody/tr[4]/td[1]/nobr/span')
# print(val3.text)
# val4 = driver.find_element_by_xpath('//*[@id="T301444200"]/tbody/tr[5]/td[1]/nobr/span')
# print(val4.text)
url1 = "https://office.live.com/start/Excel.aspx"
driver.get(url1)
driver.switch_to_frame('h_signiniframe')
driver.find_element_by_xpath('/html/body/div[2]/div/main/div[2]/div[4]/div/input').send_keys('kaushicramesh@gmail.com')
driver.find_element_by_xpath('/html/body/div[2]/div/main/div[3]/input').click()
#driver.switch_to_frame(driver.find_element_by_id('i0118'))
# driver.find_element_by_xpath('//*[@id="i0118"]').send_keys('CargillRocks11')
driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()

#
# onedrive_username = driver.find_element_by_id('signInDescription')
# onedrive_username.click()
# onedrive_username.send_keys('kaushicramesh@gmail.com')


