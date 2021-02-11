
import requests
import json
if __name__ == '__main__':
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%8D%8E%E8%AF%AD&sort=recommend&page_limit=20&page_start=20'
    params = {
        'type': 'movie',
        'tag': '华语',
        'sort': 'recommend',
        'page_limit': '20', #一次取多少个
        'page_start': '20', #从库的第几部电影去取
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    response = requests.get(url=url, params=params, headers=headers)
    #print(response.text)
    list_data = response.json()
    fp = open('douban.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print('over!!!')
    fp.close()
