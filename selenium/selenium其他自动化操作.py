from selenium import webdriver
from time import sleep
#操作淘宝页面
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://www.taobao.com/')

#标签定位
search_input = bro.find_element_by_id('q')
#search_input = bro.find_element_by_xpath('//*[@id="q"]')

#标签交互
search_input.send_keys('男装')

#执行一组js程序，滚轮滚动一屏高度
bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')
sleep(2)
#点击搜索按钮，类选择器，加'.'
search_btn = bro.find_element_by_css_selector('.btn-search')

search_btn.click()

bro.get('https://www.baidu.com/')
sleep(2)
#当前浏览器进行回退
bro.back()
#当前浏览器进行前进
sleep(2)
bro.forward()

sleep(5)
bro.quit()
