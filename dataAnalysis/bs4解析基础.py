from bs4 import BeautifulSoup
if __name__ == '__main__':
    #将本地的html文档中的数据加载到该对象中
    fp = open('./test.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    #print(soup)
    #print(soup.div) #soup.tagName 返回的是html中第一次出现的tagName标签
    #soup.find(tagName) 等同于 soup.tagName
    #print(soup.find('div')) #print(soup.div)
    #print(soup.find('div', class_='header'))
    #print(soup.find_all('div')) #返回符合要求的所有标签(列表)

    #print(soup.select('.header')) #返回
    #print(soup.select('body > div > div')[0]) #.wrapper 表示class为wrapper
    #print(soup.select('body > div div')[0]) #空格表示多个层级，> 表示一个层级
    print(soup.select('body > div div > a')[0])
    print(soup.select('body > div div')[0].text)
    print(soup.select('body > div div')[0].string)
    print(soup.select('body > div div')[0].get_text())
    print(soup.select('body > div div > a')[0]['href'])