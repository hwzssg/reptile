import re

str = './video/陈佩斯开腔 | 在历史中寻找中国喜剧的踪迹.mp4'
print(re.sub(r'|', 'a', str))