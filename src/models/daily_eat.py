from sqlalchemy import Column, Integer, String, ForeignKey
import src.orm as orm

Base = orm.Base

class DailyEat(Base):
    __tablename__ = "daily_eats"
    
    user_id = Column(String(20), primary_key=True)
    food_name = Column(String(50), ForeignKey("foods.name"))
    year = Column(Integer)
    month = Column(Integer)
    date = Column(Integer)
    count = Column(Integer, default=1) 
   
    def __init__(self, user_id, food_name, year, month, date):
        self.user_id = user_id
        self.food_name = food_name
        self.year = year
        self.month = month
        self.date = date

    def as_dict(self):
        return {
                    "user_id" : self.user_id,
                    "food_name" : self.food_name,
                    "year" : self.year,
                    "month" : self.month,
                    "date" : self.date,
                    "count" : self.count
               }
