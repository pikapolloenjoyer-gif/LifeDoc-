import claseanimal

#Programación orientada a objetos


class Database:
    def __init__(self,host,port,user,clef):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__clef = clef
    
    def get_port(self):
        return self.__port
    
    def get_user(self):
        return self.__user
    
    def get_host(self):
        return self.__host
    
    def connect(self):
        print("Connecting to database at {}:{} with user {}".format(self.__host, self.__port,self.__user))

    def disconnect(self):
        print("disconecting to database at {}:{}".format(self.__host, self.__port))

    def execute_query(self,query):
        print("Executing query:{} ".format(query))

db = Database("localhost",80,"admin","1234")
print(db.get_host())
print(db.get_port())
print(db.get_user())        
    

class MySQLDatabase(Database):
    def __init__(self, host, port, user, clef):
        super().__init__(host, port, user, clef)



