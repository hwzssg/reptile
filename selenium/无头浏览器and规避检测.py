from selenium import webdriver
from time import sleep
#实现无可视化界面
from selenium.webdriver.chrome.options import Options
#实现规避检测
from selenium.webdriver import ChromeOptions

#实现无可视化界面的操作
#无可视化界面（无头浏览器），除了谷歌还有phantomJs
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#实现让selenium规避被检测到的风险
options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
bro = webdriver.Chrome(executable_path='./chromedriver.exe'
                       , chrome_options=chrome_options
                       , options=options)
bro.get('https://ww.baidu.com')

print(bro.page_source)
sleep(2)
bro.quit()

