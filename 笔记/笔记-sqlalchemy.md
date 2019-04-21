# ORM具体步骤

1.连接指定数据库

    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///./test.db')
    #连接至同目录下的sqlite数据库,其他数据库连接方式参考文档

2.定义数据表

    from sqlalchemy import Column, String, Integer, DateTime, Boolean
    #导入数据类型,分别对应相应的数据库字段类型
    from sqlalchemy.ext.declarative import declarative_base
    #必要的基类
    Base = declarative_base()
    class NewTable(Base):
    #继承基类
        __tablename__ = 'Student'
        #定义表名
        id  = Column(Integer, primary_key=True)
        name = Column(String(100), nullable=True)
        sex = Column(String(10))
        created_time = Column(DateTime)
        is_valid  = Column(Boolean)
        #定义数据及其类型
    
3.数据库中创建表

    Base.metadata.create_all(engine)
    #把创建的表同步到数据库
    
4.写入数据

    from sqlalchemy.orm import sessionmaker
    #使用ORM功能
    Session  = sessionmaker(bind=engine)
    #绑定数据库
    class Demo():

        def __init__(self):
            self.session = Session()
    
        def addone(self):
            new_obj = NewTable(
                name='willy',
                sex='man',
                is_valid=True
            )
            #定义需要写入的数据,'NewTable'为表名
            self.session.add(new_obj)
            #在表中添加数据
            self.session.commit()
            #同步到数据库
            
5.待续...