import asyncio
import time
import requests
#使用该模块中的ClientSession对象进行网络请求发送
import aiohttp

async def get_page(url):
    print('正再下载', url)
    #使用async修饰with 表示异步上下文管理
    async with aiohttp.ClientSession() as session:
        #get() 和 post() :
        #增加headers进行UA伪装
        #get()方法中使用params，post()方法中使用data，进行参数处理
        #proxy='http://ip:port' 不是字典
        #增加await挂起网络请求中的耗时
        async with await session.get(url=url) as response:
            #text()方法返回字符串形式的响应数据
            #read()方法返回二进制形式的响应数据
            #json()返回的是json对象

            #在使用响应数据操作前一定要使用await进行手动挂起，否则会有如下报错
            #E:\Program Files (x86)\Python\lib\asyncio\events.py:126: RuntimeWarning: coroutine 'ClientResponse.text' was never awaited
            #self._callback(*self._args)
            page_text = await  response.text()
            print(page_text)
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
