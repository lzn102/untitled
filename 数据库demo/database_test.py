from sqlalchemy import create_engine

engine = create_engine('sqlite:///./test.db')


res = engine.execute('SELECT ID NAME FROM FAMILY')

print(res)