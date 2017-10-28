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
        dict_row = row.__dict__
        print(dict_row)
        dict_row.pop("_sa_instance_state")
        result.append(row.__dict__)
    return result

def as_list_dict_join(rows):
    result = []
    for row in rows:
        row_dict = {}
        for column in row:
            row_dict.update(column.__dict__)
        row_dict.pop("_sa_instance_state")
        result.append(row_dict)
    return result

