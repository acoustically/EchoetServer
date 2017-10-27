from sqlalchemy import Column, Integer, String
import src.orm as orm

Base = orm.Base

class UserBody(Base):
    __tablename__ = "user_bodys"
    
    user_id = Column(String(20), primary_key=True)
    year = Column(Integer, primary_key=True)
    month = Column(Integer, primary_key=True)
    weight = Column(Integer)
    height = Column(Integer)
   
    def __init__(self, user_id, year, month, weight, height):
        self.user_id = user_id
        self.year = year
        self.month = month
        self.weight = weight
        self.height = height

    def as_dict(self):
        return {
                    "user_id" : self.user_id,
                    "year" : self.year,
                    "month" : self.month,
                    "weight" : self.weight,
                    "height" : self.height
               }
