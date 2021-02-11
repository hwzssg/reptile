##selenium模块
###selenium模块和爬虫之间具有怎样的联系
- 便捷的获取网站中动态加载的数据
- 便捷实现模拟登录

###什么是selenium
- 基于浏览器自动化的一个模块。

###selenium使用流程：
- 环境安装: pip install selenium
- 下载一个浏览器的驱动程序(谷歌浏览器)
  1. url : 
     http://chromedriver.storage.googleapis.com/index.html
  2. 驱动程序和浏览器的映射关系：
    https://blog.csdn.net/huilan_same/article/details/51896672
  3. 通过selenium实例化一个浏览器对象
  4. 编写基于浏览器自动化的操作代码 
     4.1 发起请求：get(url)
     4.2 标签定位：find系列方法 
     4.3 标签交互：send_keys('xxx')
     4.4 执行js程序：excute_script('jsCode')
     4.5 前进，后退：back(), forward()
     4.6 关闭：quit()
  
##selenium处理iframe(页面中嵌套子页面)
- 如果定位的标签存在于iframe标签当中，必须使用switch_to.frame(id)，切换作用域
- 动作链(拖动之类):from selenium.webdriver import ActionChains
    1. 实例化一个动作链对象： action = ActionChains(bro)
    2. 长按且点击操作：action.click_and_hold(div)
    3. 拖动：action.move_by_offset(17, 0).perform()
    4. 让动作链立即执行：perform()方法
    5. 释放动作链对象：action.release()
    
##无可视化界面(无头浏览器)

##规避检测

```python
# chrome 79以前版本
from selenuim import webdriver
from selenium.webdriver import ChromeOptions
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
driver = webdriver.Chrome(options=option)
# chrome 79以后版本
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
