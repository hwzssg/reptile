from selenium import webdriver
from time import sleep
from CodeClass import Chaojiying_Client
from PIL import Image
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
#登录页面
# chrome_options = Options()
# chrome_options.add_argument('-kiosk') #是自启动全屏
# bro = webdriver.Chrome('./chromedriver.exe', chrome_options=chrome_options)
options = ChromeOptions()
bro = webdriver.Chrome('./chromedriver.exe', options=options)
bro.maximize_window() #最大化浏览器
# bro.execute_script("document.body.style.zoom='0.8'") # 125%电脑显示效果需要改下缩放比例
#规避检测
bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
bro.get('https://kyfw.12306.cn/otn/resources/login.html')
sleep(1)
bro.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()

#save_screenshot 将当前页面进行截图并保存
bro.save_screenshot('./aa.png')

#对图片进行裁剪
#确定验证码图片对应的左上角和右下角的坐标（确定裁剪的区域）
#使用location 和 size属性获取
code_img_ele = bro.find_element_by_xpath('//*[@id="J-loginImg"]')
location = code_img_ele.location    #返回验证码图片左上角坐标，location为字典类型
#print(location)
size = code_img_ele.size #验证码对应的长和宽 size也是字典类型
#print(size)
rangle = (
    int(location['x']),
    int(location['y']),
    int(location['x'] + size['width']),
    int(location['y'] + size['height']),
)
print(rangle)

i = Image.open('./aa.png')
code_img_name = './code.png'
#crop 根据指定区域进行图片裁剪
frame = i.crop(rangle)
frame.save(code_img_name)

#将验证码图片提交给超级鹰进行识别
#替换自己账号密码
chaojiying = Chaojiying_Client('xxx', 'xxx', '96001')  # 用户中心>>软件ID 生成一个替换 96001
im = open('code.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
result = chaojiying.PostPic(im, 9004) #['pic_str'] #9004 验证码格式
print(result)
result = result['pic_str']
pos_list = []
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        pos_list.append(xy_list)
else:
    xy_list = []
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list.append(x)
    xy_list.append(y)
    pos_list.append(xy_list)

print(pos_list)
#遍历列表，使用动作链对每一个列表元素对应的x，y指定的位置进行点击操作
for pos in pos_list:
    x = pos[0]
    y = pos[1]
    #切换参照物
    ActionChains(bro).move_to_element_with_offset(code_img_ele, x, y).click().perform()
    sleep(0.5)

bro.find_element_by_id('J-userName').send_keys('username')
sleep(1)
bro.find_element_by_id('J-password').send_keys('password')
sleep(1)
bro.find_element_by_id('J-login').click()
sleep(1)

#根据返回的点使坐标使用鼠标滑动并点击
#按住滑块，拖到最右，完成校验功能
slider = bro.find_element_by_xpath('//*[@id="nc_1_n1z"]')
slider_bar = bro.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
offset = slider_bar.size['width']
print(offset)
ActionChains(bro).click_and_hold(slider).move_by_offset(offset, 0).perform()
#ActionChains(bro).drag_and_drop_by_offset(slider, offset, 0).perform()
