# SQL 语句
```
CREATE DATABASE test;
GRANT ALL ON test.* to user;
USE test;
DROP DATABASE test;

CREATE TABLE users (login VARCHAR(8), uid INT, pid INT);
DROP TABLE users;
INSERT INTO users VALUES('lihua',21,1);
UPDATE users SET pid=4 WHERE pid=2;
UPDATE users SET pid=4 WHERE uid=2;
DELETE FROM users WHERE pid=2;
```



# DB-API
## 1. 模块属性
一个兼容DB-API的模块必需定义以下功能和属性。
| 属性         |描述|
| :---:        |:---:|
| apilevel     |需要适配器兼容的DB-API版本 |
| threadsafety |本模块的线程安全级别：0,1,2,3 |
| paramstyle   |本模块SQL语句的参数风格: numeric,named,pyformat,qmark,format|
| connect()    |connect函数|
| Warning      |警告异常|
| Error        |错误异常，包括Interface*; Database*:Data*,Operation*,Intergrity*,Internal*,Programming*,NotSupported*|

## 2. Connection对象
Connection应当定义以下方法。
|方法           |描述|
|:---:         |:---:|
|close()       |关闭数据库连接|
|commit()      |提交当前事务|
|rollback()    |取消当前事务|
|cursor()      |创建一个（类）游标对象|
|errorhandler()|给定连接的游标的处理程序|

## 3. Cursor对象
Cursor对象的属性和方法。
|属性和方法     |描述|
|:---:         |:---:|
|arraysize     |使用fetchmany()时取出的结果行数|
|description   |返回游标活动状态|
|lastrowid     |上次修改行的ID|
|messages      |游标执行后从数据库获得的消息列表|
|rowcount      |上次execute*()方法处理或影响的行数|
|callproc()    |调用存储过程|
|close()       |关闭游标|
|execute()     |执行数据库查询或命令|
|executemany() |为所有参数执行数据库查询或命令|
|fetchone()    |获取查询结果的下一行|
|fetchmany()   |获取查询结果的下N行|
|fetchall()    |获取查询结果所有行|

## 4. 类型对象和构造函数
为了协调python对象和数据库对象，需要创建构造函数。
|类型对象           |描述|
|:---:             |:---:|
|Date              |日期值对象|
|Time              |时间值对象|
|Timestamp         |时间戳对象|
|DateFromticks     |日期对象|
|TimeFromticks     |时间对象|
|TimestampFromticks|时间戳对象|
|Binary            |二进制字符串对象|
|STRING            |基于字符串列的对象|
|BINARY            |（长）二进制列的对象|
|NUMBER            |数值列的对象|
|DATETIME          |日期时间列的对象|
|ROWID             |行ID的对象|



# 使用适配器
- 关系型

|数据库      |适配器|
|:---:      |:---:|
|MySQL      |MySQLdb|
|PostgrepSQL|psycopg,PyPgSQL,PyGreSQL|
|SQLite     |sqlite3|

```
#MySQLdb
import MySQLdb ad mdb

cxn=mdb.connect(user='root')
cxn.query('CREATE DATABASE test')
cxn.query('GRANT ALL ON test.* to user')
cxn.commit()
cxn.close()

cxn=mdb.connect(db='test')
cur=cxn.cursor()
cur.execute('CREATE TABLE users(login VARCHAR(8), pid INT)')
cur.execute("INSERT INTO users VALUES('john',1000)"); cur.execute("INSERT INTO users VALUES('bob',2000)"); cur.execute("INSERT INTO users VALUES('jane',3000)")
cur.execute("UPDATE users SET pid=2001 WHERE pid=2000")
cur.execute("DELETE FROM users WHERE login='bob'")
cur.execute("DROP TABLE users")

cur.execute("SELECT * FROM users WHERE login LIKE 'j%'")
for data in cur.fetchall():
    print "%s\t%s" % data
    
cur.close()
cxn.commit()
cxn.close()
```

- 非关系型

|数据库      |适配器|
|:---:      |:---:|
|MongoDB    |PyMongo|



# ORM
- SQLAIchemy
- SQLObject
