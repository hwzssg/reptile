import requests
import lxml
from lxml import etree
import json
import sys


def generate_single_dp_def(code_name_max_len, code_name, desc, code_type, extra_info=''):
    prefix = '#define PREFIX_'
    ret_def = prefix + ''.join(code_name).upper()
    ret_def += ' ' * (len(prefix) + code_name_max_len - len(ret_def) + 2) + code_name
    ret_def += ' ' * (code_name_max_len - len(code_name) + 2) + '///< ' + desc + ' ' + '@remark 类型' + code_type
    if extra_info != '':
        ret_def += ' @remark 取值说明 ' + extra_info
    return ret_def


# dp为dict格式的数组
def generate_batch_dp_def(dps):
    code_name_max_len = 0
    for dp in dps:
        code_name_max_len = max(code_name_max_len, len(dp['code_name']))

    for dp in dps:
        ret = generate_single_dp_def(code_name_max_len, dp['code_name'], dp['desc'], dp['code_type'], dp['extra_info'])
        print(ret)
        # 写入文件


'''
示例代码如下：
    BOOL_T switch = true; //type name = var；
    func(str1, &switch, str3);
'''


# 定义单个dp函数调用
def generate_single_fun_call(code_name, code_type, extra_info):
    def_type = {'Boolean': 'BBB', 'Enum': 'EEE', 'Integer': 'III'}
    type_dic = {'Boolean': 'bool', 'Enum': 'char *', 'Integer': 'int'}
    ret = 'bool '
    if code_type in type_dic:
        ret = ''.join(type_dic[''.join(code_type)])

    if ret == 'bool':
        ret += (' ' + code_name + ' = true;')
    elif ret == 'char *':
        rear = '"";'
        json_info = json.loads(extra_info)
        if 'range' in json_info and len(json_info['range']) >= 1:
            rear = json_info['range'][0] = ';'
        ret += ' ' + code_name
        ret += rear
    elif ret == 'int':
        json_info = json.loads(extra_info)
        value = 0
        if 'min' in json_info and 'max' in json_info:
            value = int((json_info["min"] + json_info["max"]) / 2)
        ret += ' ' + code_name + ' = '
        ret += str(value) + ';'

    print(ret)


# 定义批量dp函数调用
def generate_batch_fun_call(dps):
    for dp in dps:
        generate_single_fun_call(dp['code_name'], dp['code_type'], dp['extra_info'])


if __name__ == '__main__':
    # 解析保存到本地的html文件
    url = 'http://127.0.0.1:8080/code/python/table.html'
    print(sys.argv[0])

    if len(sys.argv) >= 2 and ''.join(sys.argv[1]) != '':
        url = sys.argv[1]
        print(url)

    # url = 'http://127.0.0.1:8080/code/python/test.json'
    # url = 'http://www.baidu.com'

    response = requests.get(url=url)
    response.encoding = 'utf-8'
    page_text = response.text
    # print(page_text)
    tree = etree.HTML(page_text)
    tr_list = tree.xpath('/html/body/table/tbody/tr') # 测试使用，实际页面需结合情况替换

    dps = []
    for tr in tr_list:
        dp = {'code_name': ''.join(tr.xpath('./td[1]/text()')), 'desc': ''.join(tr.xpath('./td[2]/text()')),
              'code_type': ''.join(tr.xpath('./td[3]/text()')), 'extra_info': ''.join(tr.xpath('./td[4]/text()'))}
        # demo
        dps.append(dp)
        # print(dp['code_name'], dp['desc'], dp['code_type'], dp['extra_info'])

    generate_batch_dp_def(dps)

    generate_batch_fun_call(dps)
