import asyncio
async def request(url):
    print('正在请求的url是：', url)
    print('请求成功', url)
    return url
#async修饰的函数，调用之后返回的一个协程对象
c = request('www.baidu.com')

# ---------------------------------------------------
#创建一个事件循环对象
# loop = asyncio.get_event_loop()
#
# #将协程对象注册到loop中，然后启动loop，之后协程对象对应的函数将会被执行
# #run_until_complete() 既可以实现注册，同时也会启用循环
# loop.run_until_complete(c)
# ---------------------------------------------------
#task的使用
#将协程对象封装到task任务当中
# loop = asyncio.get_event_loop()
# #基于loop创建了一个task任务对象，并将协程对象封装到task对象中
# task = loop.create_task(c)
# #<Task pending coro=<request() running at D:/Code/Python/reptile/高性能异步爬虫/协程.py:2>>
# print(task) #协程状态表示未执行
# loop.run_until_complete(task)
# #<Task finished coro=<request() done, defined at D:/Code/Python/reptile/高性能异步爬虫/协程.py:2> result=None>
# print(task) #协程状态表示被执行

# ---------------------------------------------------
#future的使用，和task对象实现方式上有些区别
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task) #协程状态表示未执行
# loop.run_until_complete(task)
# print(task) #协程状态表示被执行

# ---------------------------------------------------
#任务对象执行完，执行callback_fun
def callback_fun(task):
    print(task.result())
#绑定回调
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
task.add_done_callback(callback_fun)
loop.run_until_complete(task)





