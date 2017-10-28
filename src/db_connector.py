from src.python_mysql_connector.mysql_connector import Connector

class DBConnector(Connector):
    def __init__(self):
        self.host="echoet.crsnodt9hkzk.ap-northeast-2.rds.amazonaws.com"
        self.user="acoustically"
        self.password="ECsung1031!"
        self.db="Echoet"
        Connector.__init__(self, self.host, self.user, self.password, self.db)
