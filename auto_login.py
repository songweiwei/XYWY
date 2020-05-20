from selenium import webdriver
from time import sleep
browser = webdriver.Chrome()
browser.get("http://www.xywy.com/")
browser.find_element_by_class_name("j-login-in").click()
browser.find_element_by_class_name("s-01dl-yhm").send_keys("13551169917")
browser.find_element_by_class_name("s-01dl-mm").send_keys("songwei7601159")
browser.find_element_by_class_name("s-01dl-sub").click()
cookie_items = browser.get_cookies()


cookie_str=""
for item_cookie in cookie_items:
    item_str = item_cookie["name"]+"="+item_cookie["value"]+"; "
    cookie_str += item_str
    print(item_cookie)
#打印出来看一下
print(cookie_str)
sleep(5)
browser.get_screenshot_as_file('test.png')
browser.close()


# #模拟登录方法,模拟登录yahoo邮箱
# # coding = utf-8
# #模拟浏览器自动登录yahoo邮箱
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.chrome.options import Options
#
# #一下三行为无头模式运行，无头模式不开启浏览器，也就是在程序里面运行的
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# browser = webdriver.Chrome(executable_path=(r'C:\Users\0923\AppData\Local\Google\Chrome\Application\chromedriver.exe'), options=chrome_options)
# # #如果不用上面三行，那么就用下面这一行。运行的时候回自动的开启浏览器，并在浏览器中自动运行，你可以看到自动运行的过程
# # browser = webdriver.Chrome(executable_path=(r'C:\Users\0923\AppData\Local\Google\Chrome\Application\chromedriver.exe'))
# #设置访问链接
# browser.get("https://www.yahoo.com")
# #点击登录按钮
# browser.find_element_by_id("uh-signin").click()
# #输入用户名
# browser.find_element_by_id("login-username").send_keys("bjs***99")
# #点击“下一步”
# browser.find_element_by_id("login-signin").click()
# #等待10秒，以防读取不到（#login-passwd）元素
# sleep(10)
# #输入密码
# browser.find_element_by_id("login-passwd").send_keys("Zf***234")
# #点击signin按钮
# browser.find_element_by_id("login-signin").click()
# #获取cookie
# cookie_items = browser.get_cookies()
# cookie_str = ""
# #组装cookie字符串
# for item_cookie in cookie_items:
#     item_str = item_cookie["name"]+"="+item_cookie["value"]+"; "
#     cookie_str += item_str
#     print(item_cookie)
# #打印出来看一下
# print(cookie_str)
# sleep(5)
# browser.get_screenshot_as_file('test.png')
# browser.close()
# print('test!')





# #方法三：模拟登陆获得cookies
# # -*- coding:utf-8 -*-
# import json
# import time
#
# from pyvirtualdisplay import Display
# import schedule
# from selenium import webdriver
# import requests
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.chrome.options import Options
#
# options = webdriver.ChromeOptions()
# display = Display(visible=0, size=(800, 600))
# display.start()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
#
# chrome_drive = '/usr/bin/chromedriver'
# url = "https://cas.admore.com.cn/login?service=https%3A%2F%2Fadwords.admore.com.cn%2F"
# driver = webdriver.Chrome(executable_path=chrome_drive, chrome_options=options)
#
#
# def get():
#     print(12345678)
#     print(12345678)
#     print(12345678)
#     print(12345678)
#     time.sleep(10)
#     driver.get("https://adwords.admore.com/main")
#     print(1111, driver.page_source)
#     cookies = driver.get_cookies()
#     print(cookies)
#     if len(cookies) == 6:
#         print(cookies)
#         with open("shike_cokkies.txt", "w") as f:
#             json.dump(cookies, f)
#     #    return driver
#     else:
#         print(987654321)
#         driver.set_page_load_timeout(10)
#         driver.get(url)
#         time.sleep(5)
#         print("asdfgh")
#         name_input = driver.find_element_by_id('username')  # 找到用户名的框框
#         pass_input = driver.find_element_by_id('userInputPassword')  # 找到输入密码的框框
#         login_button = driver.find_element_by_xpath('//*[@id="checkFormInput"]/input[4]')
#         # action2 = driver.find_element_by_name("login")
#         # ActionChains(driver).move_to_element(name_input)
#         name_input.clear()
#         time.sleep(1)
#         # time.sleep(5)
#         name_input.send_keys('账号')  # 填写用户名
#         pass_input.clear()
#         # ActionChains(driver).move_to_element(pass_input)
#         time.sleep(1)
#         pass_input.send_keys('密码')  # 填写密码
#         # time.sleep(5)
#         # js = "window.scrollTo(0,document.body.scrollHeight)"
#         # driver.execute_script(js)
#         # ActionChains(driver).move_to_element(login_button)
#         login_button.click()
#         # WebDriverWait(driver, 300000000).until_not(lambda x: x.find_element_by_class_name("hot-item ng-binding ng-scope").is_displayed())  # 等待直到登录成功
#         # print(34556)
#         # second_logng = driver.find_element_by_class_name("pull-right login")
#         # ActionChains(driver).move_to_element(action2).click(action2).perform()
#         # second_logng.click()
#         # driver.get("https://adwords.admore.com/main")
#         # sedssion = driver.get_cookie("SESSION")
#         time.sleep(1)
#         driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div[3]/a").click()
#         # AGL_USER_ID = driver.get_cookie("AGL_USER_ID")
#         # driver.find_element_by_xpath("//*[@id="myHeader"]/div[3]/div[1]/div/div[2]/a[2]")
#         driver.get("https://adwords.admore.com/main")
#         # print(driver.page_source)
#         # ddict = {}
#         # print(driver.get_cookies())
#         # print(sedssion,AGL_USER_ID)
#         cokies_list = []
#         if '账户总览' in driver.page_source:
#             print("登录成功!")
#             cokies_list = driver.get_cookies()
#             print(cokies_list)
#         else:
#             print("结束")
#         # driver.quit()
#         with open("shike_cokkies.txt", "w") as f:
#             json.dump(cokies_list, f)
#     # display.stop()
#
#
# # schedule.every().day.at("00:30").do(get)
# # schedule.every().day.at("12:00").do(get)
# ##schedule.every().day.at("22:00").do(get)
# schedule.every().hour.do(get)
# while True:
#     schedule.run_pending()
#     time.sleep(3)
# # for i in range(2):
# # get()
# # get()













































