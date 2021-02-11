import asyncio
import time
import requests

#import aiohttp

async def get_page(url):
    print('正再下载', url)
    #requests.get()请求是基于同步的，必须使用基于异步的网络请求模块进行指定url的发送请求
    #aiohttp:基于异步网络模块的请求
    response = requests.get(url=url)
    print(response.text)
    print('下载完毕', url)

start = time.time()
urls = [
    'http://127.0.0.1:5000/wang1',
    'http://127.0.0.1:5000/wang2',
    'http://127.0.0.1:5000/wang3',
]
tasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print(time.time() - start) #6s 还是串行耗时
