import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    url = 'https://www.baidu.com/s?wd=ip'
    #response = requests.get(url=url, headers=headers)
    response = requests.get(url=url, headers=headers, proxies={'https': '163.204.95.242:9999'}) #代理失效
    response.encoding = 'UTF-8'
    page_text = response.text
    print(page_text)
    with open('ip.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
