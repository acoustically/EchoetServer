from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://acoustically:ECsung1031!@echoet.crsnodt9hkzk.ap-northeast-2.rds.amazonaws.com/Echoet")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

def as_list_dict(rows):
    result = []
    for row in rows:
        result.append(row.as_dict())
    return result

