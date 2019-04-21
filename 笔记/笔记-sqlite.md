# python使用sqlite3模块连接（创建）数据库

conn = sqlite3.connect('test.db')


# sqlite3数据库创建表

CREATE TABLE TABLE_NAME (
    数据表名称    数据类型    是否允许为空     是否为主键         ,
    ID                INT           NUT NULL         PRIMARY KEY    ,
    NAME            TEXT         默认不允许        默认不设主键      ,
    ADDRESS      CHAR(30)                                                  ,
    EMAIL          REAL             
) 

# sqlite数据库插入数据

INSERT INTO TABLE_NAME(
    ID, NAME, ADDRESS, EMAIL "需要插入的数据"
    ) VALUES(
    1, 'Willy'， 'China'， name@163.com "与上面对应，字符类型要加引号"
    )

# sqlite数据库选取数据

SELECT ID, NAME, ADDRESS, EMAIL FROM TABLE_NAME "按需填写选择数据"

# sqlite数据库更新数据

UPDATE TABLE_NAME set ADDRESS = 'England' where ID = 1

# sqlite数据库删除数据

DELETE from TABLE_NAME where ID=1


# 笔记参考地址
[参考](http://www.runoob.com/sqlite/sqlite-python.html)