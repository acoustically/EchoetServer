from sqlalchemy import Column, Integer, String
import src.orm as orm

Base = orm.Base

class DailyEat(Base):
    __tablename__ = "daily_eats"
    
    user_id = Column(String(20), primary_key=True)
    food = Column(String(50))
    year = Column(Integer)
    month = Column(Integer)
    date = Column(Integer)
    
    def __init__(self, user_id, food, year, month, date):
        self.user_id = user_id
        self.food = food
        self.year = year
        self.month = month
        self.date = date

    def as_dict(self):
        return {
                    "user_id" : self.id,
                    "food" : self.password
                    "year" : self.year
                    "month" : self.month
                    "date" : self.date
               }
