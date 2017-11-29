from src.common.database import Database

class Profile(object):
    def __init__(self, port_id, user_email, name, Y, T, dis_inc, init_con, goal, importance, r1, r2, r3, r4, r5):
        self.port_id = port_id
        self.user_email = user_email
        self.name = name
        self.Y = Y
        self.T = T
        self.dis_inc = dis_inc
        self.init_con = init_con
        self.goal = goal
        
        if int(Y) <= 1:
            t = 1
        elif int(Y) <=2:
            t = 2
        elif int(Y) <= 5:
            t = 3
        elif int(Y) <= 10:
            t = 4
        else:
            t = 5
        
        time = (6 - int(importance) + t)/2
        risk = (int(r1)+int(r2)+int(r3)+int(r4)+int(r5))*2
        
        if time <= 1:
            if risk <= 18:
                profile = "Conservative"
            elif risk <= 31:
                profile = "Moderately Conservative"
            else:
                profile = "Moderate"
                
        elif time <= 2:
            if risk <= 15:
                profile = "Conservative"
            elif risk <= 24:
                profile = "Moderately Conservative"
            elif risk <= 35:
                profile = "Moderate"
            else:
                profile = "Moderately Aggressive"
                
        elif time <= 3:
            if risk <= 12:
                profile = "Conservative"
            elif risk <= 20:
                profile = "Moderately Conservative"
            elif risk <= 28:
                profile = "Moderate"
            elif risk <= 37:
                profile = "Moderately Aggressive"
            else:
                profile = "Aggressive"
        
        elif time <= 4:
            if risk <= 11:
                profile = "Conservative"
            elif risk <= 18:
                profile = "Moderately Conservative"
            elif risk <= 25:
                profile = "Moderate"
            elif risk <= 34:
                profile = "Moderately Aggressive"
            else:
                profile = "Aggressive"
                
        else:
            if risk <= 10:
                profile = "Conservative"
            elif risk <= 17:
                profile = "Moderately Conservative"
            elif risk <= 24:
                profile = "Moderate"
            elif risk <= 31:
                profile = "Moderately Aggressive"
            else:
                profile = "Aggressive"
        
        if profile == "Conservative":
            self.init_alloc = [0.15,0,0.05,0.25,0.25,0.3]
            self.lamb = 1.00
        elif profile == "Moderately Conservative":
            self.init_alloc = [0.25,0.05,0.10,0.25,0.25,0.10]
            self.lamb = 0.75
        elif profile == "Moderate":
            self.init_alloc = [0.35,0.10,0.15,0.175,0.175,0.05]
            self.lamb = 0.50
        elif profile == "Moderately Aggressive":
            self.init_alloc = [0.45,0.15,0.20,0.075,0.075,0.05]
            self.lamb = 0.25
        else:
            self.init_alloc = [0.50,0.20,0.25,0,0,0.05]
            self.lamb = 0.00

    def json(self):
        return {
            "port_id": self.port_id,
            "user_email": self.user_email,
            "name": self.name,
            "goal": self.goal,
            "length_of_goal": self.Y,
            "length_remaining": self.T,
            "init_con": self.init_con,
            "dis_inc": self.dis_inc,
            "init_alloc": self.init_alloc,
            "lamb": self.lamb
        }

    def save_to_mongo(self):
        Database.insert("profiles", self.json())

   
    @staticmethod
    def from_mongo(port_id):
        data = Database.find_one(collection="profiles", query={'port_id': port_id})
        if data is not None:
            return data

    @staticmethod
    def delete_profile(port_id):
        Database.delete_all(collection="profiles", query ={"port_id": port_id})
   
    @staticmethod
    def update_profile(port_id, query):
        # query must include all the fields of profiles
        Database.update("profiles", {"port_id": port_id}, query)
