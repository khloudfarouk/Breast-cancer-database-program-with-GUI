# Breast-cancer-database-program-with-GUI
breast cancer database using GUI with some options the user can make : query on database , insert fields in database ,delete fields , updating them , making index on fields , making aggregation on them , using pymongo and mongodb


before run this code make sure you have a database on mongodb and modify the client line with your client like this :      `self.client = MongoClient('mongodb://localhost:27017/')
self.db = self.client['BrastCancer']` 
and the database on mongo must contains the 3 collections on it
