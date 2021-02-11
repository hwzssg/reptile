from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

bro = webdriver.Chrome('./chromedriver.exe')
bro.get('https://qzone.qq.com')
bro.switch_to.frame('login_frame')

user_passwd_enter = bro.find_element_by_id('switcher_plogin')
user_passwd_enter.click()

userName_tag = bro.find_element_by_id('u')
userName_tag.send_keys('1234568') #用户名
sleep(1)
password_tag = bro.find_element_by_id('p')
password_tag.send_keys('1234568') #密码
sleep(1)
login_button = bro.find_element_by_id('login_button')
login_button.click()
#会有滑动块验证码验证
sleep(3)
bro.quit()


