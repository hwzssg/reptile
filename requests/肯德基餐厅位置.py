import requests
import json
if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data = {
        'cname': '',
        'pid': '',
        'keyword': '北京',
        'pageIndex': '2',
        'pageSize': '10',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    response = requests.post(url=url, headers=headers, data=data)
    text = response.text
    print(text)
    with open('肯德基.txt', 'w', encoding='utf-8') as fp:
        fp.write(text)
        fp.close()
    #list_data = response.json()
    #print(list_data)
    #fp = open('肯德基1.json', 'w', encoding='utf-8')
    #json.dump(list_data, fp=fp, ensure_ascii=False)
    #fp.close()
    print('over!!!')
