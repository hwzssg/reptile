import requests
import json
import time
#url:http://scxk.nmpa.gov.cn:81/xk/

#ajax 请求的数据
if __name__ == '__main__':
    #url = 'http://scxk.nmpa.gov.cn:81/xk/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    #静态界面获取到的数据
    #page_text = requests.get(url=url, headers=headers).text
    #with open('化妆品.html', 'w', encoding='utf-8') as fp:
    #    fp.write(page_text)

    #动态加载出来的数据，批量获取不同企业的id
    id_list = []  # 存储企业ID
    for page in range(1, 6):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname':'',
            'applysn':'',
        }
        time.sleep(3)
        json_ids = requests.post(url=post_url, headers=headers, data=data).json()
        #print(json_ids)
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
        #print(id_list)

    #获取企业详情数据
    #get_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?' #拼接id值
    all_data_list = [] #存储所有企业详情数据
    real_post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById' #通过id区分
    for id in id_list:
        data = {
            'id': id,
        }
        detail_json = requests.post(url=post_url, headers=headers, data=data).json()
        all_data_list.append(detail_json)
        time.sleep(3)
        #print(detail_json)
    #print('------------------------over!!!')
    #持久化存储
    fp = open('allData.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
    fp.close()
    print('over!!!')
