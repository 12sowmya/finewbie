import uuid
from src.common.database import Database


class Portfolio(object):
    def __init__(self,name,port_id=None):
        self.port_id = uuid.uuid4().hex if port_id is None else port_id
        self.mean_term_wealth = mean_term_wealth
        self.mean_var_wealth = mean_var_wealth
        self.alloc_percent = alloc_percent
        self.shares = shares
        self.P = P
        self.reached = reached
        self.ambitious = ambitious
        
        
    def json(self):
        return {
            "port_id": self.port_id,
            "mean_term_wealth": self.mean_term_wealth,
            "mean_var_wealth": self.mean_var_wealth,
            "alloc_percent": self.alloc_percent,
            "shares": self.shares,
            "P": self.P,
            "reached": self.reached,
            "ambitious": self.ambitious
            
        }

    def save_to_mongo(self):
        Database.insert("portfolios", self.json())

    #@classmethod
    @staticmethod
    def from_mongo(port_id):
        port_data = Database.find_one(collection='portfolios', query={'port_id': port_id})
        if port_data is not None:
            return port_data

    @staticmethod
    def delete_portfolio(port_id):
        Database.delete_all(collection='portfolios', query={"port_id": port_id})
