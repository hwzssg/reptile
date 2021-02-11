##目的
在爬虫中使用异步实现高性能的数据爬取操作。

##异步爬虫的方式：
- 多线程，多进程：
    好处：可以为相关阻塞的操作单独开启线程或者进程，阻塞的操作就可以异步执行。
    弊端：无法无限制开启多线程、多进程。
- 线程池、进程池：
    好处：可以降低系统对进程或者线程创建和销毁的频率，从而很好的降低系统的开销。
    弊端：池中线程或者进程的数量是有上限的。
 - 单线程+异步协程(推荐)：
    1. event_loop:事件循环
    2. coroutine:协程对象，我们可以将协程对象注册到时间循环中，它会被时间循环调用，
       我们可以使用async关键字来定义一个方法，这个方法在调用时不会立即被执行，而是
       返回一个协程对象。
    3. task:任务，他是对协程对象的进一步封装，包含了任务的各个状态。
    4. future:代表将来执行或者还没有执行的任务，实际上和task没有本质区别。
    5. async:定义一个协程。
    6. await:用来挂起阻塞方法的执行。
##模块引用
from multiprocessing.dummy import Pool
pool = Pool(4)
ret = pool.map(get_page, name_list)

'<video webkit-playsinline="" playsinline="" x-webkit-airplay="" autoplay="autoplay" style="width: 100%; height: 100%;" src="https://video.pearvideo.com/mp4/third/20210209/cont-1719903-10008579-105404-hd.mp4"></video>'
正则解析到"https://video.pearvideo.com/mp4/third/20210209/cont-1719903-10008579-105404-hd.mp4"
ex = 'src="(.*?)"></video>'
