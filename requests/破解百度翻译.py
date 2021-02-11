import requests
import json
# 百度翻译实际发送翻译过程
# 需要发送post请求
# 响应数据是一组json数据
if __name__ == '__main__':
    #1.指定url
    postUrl = 'https://fanyi.baidu.com/sug'

    #2.进行UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    #3.post请求参数处理(同get请求一致)
    word = input('enter a word:')
    data = {
        'kw': word
    }
    #4.请求数据
    response = requests.post(url=postUrl, data=data, headers=headers)
    #5.获取响应数据:json()方法，返回的是obj(如果确认响应数据是json类型的，才可以使用json()方法)
    dic_obj = response.json()
    print(dic_obj)

    #进行持久化存储
    fileName = word + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    fp.close()
    print('over!!!')
