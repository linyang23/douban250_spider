import sqlite3

#连接并打开数据库
conn = sqlite3.connect("./test/test.db")
print("Opened database successfully")
#操作数据库
c = conn.cursor()   #获取游标
sql = ""
c.execute(sql)  #执行sql语句
conn.commit()   #提交数据库操作
conn.close()    #关闭数据库连接