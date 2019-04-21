from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Boolean
import time

engine = create_engine('sqlite:///./test.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)


# 入库表
class InboundTable(Base):
    __tablename__ = 'InboundTable'

    time = Column(DateTime)
    address  = Column(String)
    principal =  Column(String(20))
    source  = Column(String(200))


if __name__ == '__main__':
    # res = Base.metadata.create_all(engine)
    pass

