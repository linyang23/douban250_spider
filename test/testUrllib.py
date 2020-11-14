import urllib.parse
import urllib.request

# 读取网页
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode('utf-8'))

# 将获取的网页写入html文件
# 注：response.read()只能使用一次，若上面print语句执行，则下方写入的信息为空
with open("./test/baidu.html", 'w', encoding='utf-8') as lines:
    lines.write(str(response.read().decode('utf-8')))

# 使用httpbin.org进行访问响应测试

# 获取一个post请求
data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding='utf-8')
response = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(response.read().decode('utf-8'))

# 获取一个get请求
response = urllib.request.urlopen("http://httpbin.org/get")
print(response.read().decode('utf-8'))

# # 超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("timeout!")

# 伪装信息
url = "http://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
data = bytes(urllib.parse.urlencode({'name': 'eric'}), encoding='utf-8')
req = urllib.request.Request(
    url=url, data=data, headers=headers, method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))

# 豆瓣实战
url = "http://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
