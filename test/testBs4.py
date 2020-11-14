# BeautifulSoup4将html文档转化为复杂的树形结构
# 每个节点都是python对象：Tag+NavigableString+BeautifulSoup+Comment
from bs4 import BeautifulSoup

file = open('./test/baidu.html', 'rb')
html = file.read()
bs = BeautifulSoup(html, 'html.parser')

# 捕获首个标签及其内容(Tag)
print(bs.title)
print(bs.a)
print(bs.head)

# 捕获首个标签里的内容(NavigableString)
print(bs.title.string)

# 捕获首个标签内的属性(返回一个字典)
print(bs.a.attrs)

# 捕获整个文档(BeautifulSoup)
print(bs)
print(bs.name)
print(bs.attrs)

# 捕获注释(Comment)
