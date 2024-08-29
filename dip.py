from abc import ABC, abstractmethod

class SQLDatabase:
    def save(self, data):
        print("Saving data to SQL database...")


class Order:
    def __init__(self, database: SQLDatabase):
        self.database = database

    def save_order(self, data):
        self.database.save(data)


class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


class SQLDatabase(Database):
    def save(self, data):
        print("Saving data to SQL database...")


class Order:
    def __init__(self, database: Database):
        self.database = database

    def save_order(self, data):
        self.database.save(data)

"""
The Order class now depends on the Database interface (abstraction), 
which allows for different database implementations 
(e.g., SQLDatabase, NoSQLDatabase) to be used without modifying the Order class.
"""
