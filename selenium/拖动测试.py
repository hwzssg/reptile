from selenium import webdriver
from time import sleep
# 导入动作链对应的类
from selenium.webdriver import ActionChains

bro = webdriver.Chrome('./chromedriver.exe')

url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'

bro.get(url)

#如果想要定位的标签是存在与iframe中，直接使用find系列函数无法定位
#需要使用swith_to.frame()定位，切换浏览器标签定位的作用域
bro.switch_to.frame('iframeResult')
div = bro.find_element_by_id('draggable')
print(div)

#拖动需要运动到动作链
action = ActionChains(bro)

#点击 + 长按 指定的标签
action.click_and_hold(div)
for i in range(5):
    #perform()立即执行动作链操作
    action.move_by_offset(17, 0).perform()
    sleep(0.3)
action.reset_actions()

bro.quit()
sleep(5)
