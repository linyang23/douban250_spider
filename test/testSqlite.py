import sqlite3

#连接并打开数据库
conn = sqlite3.connect("./test/test.db")
print("Opened database successfully")
#操作数据库
c = conn.cursor()   #获取游标
sql = '''
    create table company
        (id int primary key not null,
        name text not null,
        age int not null,
        address char(50),
        salary real
        );
'''
c.execute(sql)  #执行sql语句
conn.commit()   #提交数据库操作
conn.close()    #关闭数据库连接
print("成功建表")
#插入数据
conn = sqlite3.connect("test.db")
print("成功打开数据库")
c = conn.cursor()   #获取游标
sql = '''
    insert into company (id,name,age,address,salary)
    values (1, "张三", 32, "成都", 8000)
        );
'''
c.execute(sql)  #执行sql语句
conn.commit()   #提交数据库操作
conn.close()    #关闭数据库连接
print("成功建表")