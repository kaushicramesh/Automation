from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('/Applications/chromedriver')
url = "https://itsmweb.cargill.com"
driver.get(url)
username = driver.find_element_by_id('username-id')
username.send_keys('k685217')
password = driver.find_element_by_id('pwd-id')
password.send_keys('ImbeFruit11')
driver.find_element_by_name('login').click()
driver.implicitly_wait(10)
req_id_fir = '//*[@id="T301444200"]/tbody/tr['
req_id_first = req_id_fir.replace('"', "'")
req_id_second = '2'
req_id_third = ']/td[1]/nobr/span'
req_final = '"' + req_id_first + req_id_second + req_id_third + '"'
req = str(req_final)
print(req)
valu = driver.find_element_by_xpath(req)
print(valu.text)

# if driver.find_element_by_xpath('req_final').is_displayed():
#     valu = driver.find_element_by_id('req_final').is_displayed()
#     print(valu.text)
#     req_id_second = req_id_second + 1
# else:
#     print("no more requests")




# req_id = '//*[@id="T301444200"]/tbody/tr[2]/td[1]/nobr/span'

#driver.find_element_by_id('reg_img_304316340').click()

# driver.find_element_by_id('//*[@id="T301444200"]/tbody').get_property()
#
# //*[@id="T301444200"]/tbody







# driver.implicitly_wait(10)
# tot = driver.find_element_by_xpath('//*[@id="WIN_2_301444200"]/div[1]/table/tbody/tr/td[1]')
# print(tot.text)
# driver.find_element_by_xpath('//*[@id="WIN_0_80077"]/fieldset/div/div/div/div[10]/a/span').click()
# driver.find_element_by_xpath('')
# driver.find_element_by_xpath('//*[@id="WIN_0_80077"]/fieldset/div')





# total_req = driver.find_element_by_xpath('//*[@id="WIN_2_301444200"]/div[1]/table/tbody/tr/td[1]')
# print(total_req.text)
#
#
#
# //*[@id="WIN_0_80077"]/fieldset/div
# //*[@id="WIN_0_80077"]/fieldset/div/div/div/div[10]



#inc = driver.find_element_by_xpath('//*[@id="T301444200"]/tbody/tr[2]/td[1]/nobr/span')
# actionChains = ActionChains(driver)
# actionChains.double_click(inc).perform()
# driver.implicitly_wait(15)
# change_id = driver.find_element_by_id('arid_WIN_3_1000000182')
# driver.implicitly_wait(10)
# chan = actionChains.double_click(change_id).perform()
# changed_id = driver.find_element_by_id('arid_WIN_3_1000000182').text
# print(inc.text)
# inc2 = driver.find_element_by_xpath('//*[@id="T301444200"]/tbody/tr[3]/td[1]/nobr/span')
# print(inc2.text)
# status = driver.find_element_by_xpath('//*[@id="T301444200"]/tbody/tr[2]/td[6]/nobr/span')
# print(status.text)



# //*[@id="T301444200"]/tbody/tr[2]/td[1]/nobr/span

#change_id = driver.find_element_by_xpath('//*[@id="arid_WIN_3_1000000182"]').text
# val = actionChains.double_click(change_id).perform()
# print(change_id)
# status = driver.find_element_by_xpath('//*[@id="arid_WIN_3_303502600"]').text
# print(status)

#change_id = driver.find_element_by_xpath('//*[@id="arid_WIN_3_1000000182"]')



#//*[@id="arid_WIN_3_303502600"]

#
#
# //*[@id="arid_WIN_3_1000000182"]
#
#
# //*[@id="arid_WIN_3_1000000000"]




# inc_xpath = '//*[@id="T301444200"]/tbody/tr[2]/td[1]/nobr/span'
#
#
#
#
#
#
#
# driver.find_element_by_class_name('TableHdrl').get_attribute()



#
#
# //*[@id="T302087200"]/tbody/tr[2]/td[1]/nobr/span
# //*[@id="T302087200"]/tbody/tr[3]/td[1]/nobr/span
# //*[@id="T302087200"]/tbody/tr[18]/td[1]/nobr/span
# //*[@id="WIN_3_302087200"]/div[1]/table/tbody/tr/td[1]
#
#
#
#
#
# //*[@id="T301444200"]/tbody/tr[2]/td[1]/nobr/span

# driver.find_element_by_xpath('//*[@id="arid_WIN_2_303174300"]').click()
# #select = Select(driver.find_element_by_xpath('//*[@id="arid_WIN_2_303174300"]'))
# label = driver.find_elements_by_class_name('MenuEntryName')
# print(label)

# for label in labels:
#     select.select_by_visible_text('Assigned To All My Groups')
#
#
#
# //*[@id="arid_WIN_2_303174300"]


#driver.find_element_by_name('Assigned To All My Groups').click()


#driver.find_element_by_xpath('//*[@id="arid_WIN_2_303174300"]').click()



# assigned = driver.find_element_by_xpath('//*[@id="arid_WIN_2_303174300"]')
# assigned.selectByValue("Assigned To All My Groups")

#
# driver.find_element_by_id('arid_WIN_2_303174300').click()
# driver.find_element_by_link_text('Assigned To All My Groups').click()
#
#
# //*[@id="arid_WIN_2_303174300"]
# //*[@id="arid_WIN_2_1000000720"]
# /html/body/div[3]/div[2]/table/tbody/tr[4]/td[1]
# /html/body/div[3]/div[2]/table/tbody/tr[4]/td[1]
# /html/body/div[3]/div[2]/table/tbody/tr[4]/td[2
# ]

