import requests
from lxml import etree
from CodeClass import Chaojiying_Client
import re

if __name__ == '__main__':
    #将验证码下载到本地
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    #使用session，存储cookie
    session = requests.Session()
    response = session.get(url=url, headers=headers)
    response.encoding = 'UTF-8'
    page_text = response.text
    #解析额外post携带数据
    VIEWSTATE = re.findall(r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)" />', page_text, re.I)[0]
    __VIEWSTATEGENERATOR = re.findall(r'input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*?)" />', page_text, re.I)[0]
    print(VIEWSTATE, __VIEWSTATEGENERATOR)

    #解析验证码图片img中的src属性
    tree = etree.HTML(page_text)
    code_img_url = 'https://so.gushiwen.cn/' + tree.xpath('//*[@id="imgCode"]/@src')[0]
    img_data = session.get(url=code_img_url, headers=headers).content
    #验证码保存到本地
    with open('./code.jpg', 'wb') as fp:
        fp.write(img_data)

    #调用打码平台的示例程序进行验证码图片数据识别
    #输入超级鹰账号密码
    chaojiying = Chaojiying_Client('xxx', 'xxx', '96001')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('code.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    code_info = chaojiying.PostPic(im, 1902)
    print(code_info)
    #小写改成大写
    code = code_info['pic_str'].upper()
    print(code)

    #实际登录操作
    login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
    data = {
        '__VIEWSTATE': VIEWSTATE,
        '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': 'xxx.com', #使用自己账号
        'pwd': 'xxxx', #使用自己密码
        'code': code,
        'denglu': '登录',
    }
    response = session.post(url=login_url, headers=headers, data=data)
    print(response.status_code)
    with open('gushici2.html', 'w', encoding='utf-8') as fp:
        fp.write(response.text)


