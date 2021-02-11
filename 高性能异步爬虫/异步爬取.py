import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
urls = [
    'https://downsc.chinaz.net/Files/DownLoad/jianli/202102/jianli14566.rar',
    'https://downsc.chinaz.net/Files/DownLoad/jianli/202102/jianli14567.rar',
    'https://downsc.chinaz.net/Files/DownLoad/jianli/202102/jianli14564.rar',
]

def get_content(url):
    print('正在爬取', url)
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.content

def parse_content(name, content):
    print(len(content))
    #with open(name, 'wb') as fp:
    #    fp.write(content)


for url in urls:
    content = get_content(url)
    file_name = url.split('/')[-1]
    parse_content(file_name, content)


