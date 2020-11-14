import re  # 正则搜索
import urllib.request
import urllib.error  # 制定URL
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作

from bs4 import BeautifulSoup  # 网页解析

# 定义正则匹配对象
findLink = re.compile(r'<a href="(.*?)">')  # 正则匹配影片详情链接
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S) # 正则匹配图片链接,re.S实现让换行符包含在字符中
findTitle = re.compile(r'<span class="title">(.*?)</span>')  # 正则匹配影片片名
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')  # 正则匹配影片评分
findJudge = re.compile(r'<span>(\d*)人评价</span>')  # 正则匹配评价人数
findInq = re.compile(r'<span class="inq">(.*?)</span>')  # 正则匹配影片概况
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)  # 正则匹配影片相关内容

# 主函数
def main():
    baseurl = "https://movie.douban.com/top250?start="
    savepath = "./豆瓣电影Top250.xls"
    # 爬取网页并解析
    datalist = getData(baseurl)
    # 保存数据
    saveData(datalist, savepath)

# 爬取和解析网页实现
def getData(baseurl):
    datalist = []
    # 得到网页内容
    for i in range(0, 250, 25):  # 调用获取页面信息的函数，共10页
        url = baseurl + str(i)
        html = askURL(url)
        # 解析网页内容
        datalist = solveData(datalist, html)
    return datalist

# 得到网页内容实现
def askURL(url):
    head = {  # 模拟浏览器头部信息，以免被认出是爬虫程序(403)
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
    req = urllib.request.Request(url, headers=head)
    html = ""
    try:  # 异常捕捉
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html

# 解析网页内容实现
def solveData(datalist, html):
    soup = BeautifulSoup(html, "html.parser")
    # 查找符合要求（div+class="item"）的字符串形成列表
    for item in soup.find_all("div", class_="item"):
        data = []  # 用于存储数据
        item = str(item)
        # 添加详情链接
        link = re.findall(findLink, item)[0]  # findall的结果为一个item中所有匹配项的列表
        data.append(link)
        # 添加图片链接
        imgSrc = re.findall(findImgSrc, item)[0]
        data.append(imgSrc)
        # 添加影片片名
        title = re.findall(findTitle, item)
        data.append(title[0])  # 添加中文名
        if len(title) >= 2:
            data.append(title[1].replace('/', ''))  # 添加外文名
        else:
            data.append(' ')  # 添加空外文名
        # 添加影片评分
        rating = re.findall(findRating, item)[0]
        data.append(rating)
        # 添加影片评价人数
        judge = re.findall(findJudge, item)[0]
        data.append(judge)
        # 添加影片评价概况
        inq = re.findall(findInq, item)
        if len(inq):
            data.append(inq[0].replace('。', ''))  # 去掉句号
        else:
            data.append(' ')
        # 添加影片相关内容
        bd = re.findall(findBd, item)[0]
        bd = re.sub('<br(\s+)?/>(\s+)?', "", bd)  # 正则替换，去掉<br/>
        bd = re.sub('/', " ", bd)  # 去掉/符号
        data.append(bd.strip())
        datalist.append(data)
    return datalist

# 保存数据实现
def saveData(datalist, savepath):
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0) # 创建excel文件
    worksheet = workbook.add_sheet('豆瓣电影250', cell_overwrite_ok=True)   # 创建sheet命名为豆瓣电影250
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外文名", "影片评分", "评价人数", "概况", "相关信息")
    for i in range(0, 8):
        worksheet.write(0, i, col[i])  # 列名
    for i in range(0, 250): #读入之前爬取的数据
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            worksheet.write(i + 1, j, data[j])
    print("爬取完成")
    workbook.save(savepath) #保存操作

# 入口
if __name__ == "__main__":
    main()
