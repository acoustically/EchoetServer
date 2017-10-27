from sqlalchemy import Column, Integer, String
import src.orm as orm

Base = orm.Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(String(20), primary_key=True)
    password = Column(String(512))
    
    def __init__(self, id, password):
        self.id = id
        self.id = password

    def as_dict(self):
        return {
                    "id" : self.id,
                    "password" : self.password
               }
