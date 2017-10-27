from sqlalchemy import Column, Integer, String
import src.orm as orm

Base = orm.Base

class Food(Base):
    __tablename__ = "foods"
    
    name = Column(String(20), primary_key=True)
    kcal = Column(Integer)
    co2 = Column(Integer)
   
    def __init__(self, name, kcal, co2):
        self.name = name
        self.kcal = kcal
        self.co2 = co2

    def as_dict(self):
        return {
                    "name" : self.name,
                    "kcal" : self.kcal,
                    "co2" : self.co2,
               }
