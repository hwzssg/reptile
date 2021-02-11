#单线程串行
#import time
# def get_page(str):
#     print('downloading...:', str)
#     time.sleep(2)
#     print('success:', str)
#
# name_list = ['1', '2', '3', '4']
#
# start_time = time.time()
#
# for i in range(len(name_list)):
#     get_page(name_list[i])
#
# end_time = time.time()
#
# print('%d second' % (end_time - start_time))

import time
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
def get_page(str):
    print('downloading...:', str)
    time.sleep(2)
    print('success:', str)
    return str

name_list = ['1', '2', '3', '4']

start_time = time.time()

#实例化一个线程池对象
pool = Pool(4)
#将列表中每一个列表元素传递给get_page进行处理
ret = pool.map(get_page, name_list)
print(ret)
end_time = time.time()
print('%d second' % (end_time - start_time))
