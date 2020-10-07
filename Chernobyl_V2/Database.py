import sqlite3 as db

#db_path = '/home/pi/Python/Chernobyl_V2/db/Chernobyl.db'

class Database:
    
    def __init__(self, path, command):
        self.path = path
        self.command = command
        self.connection = db.connect(self.path)
        if self.connection:
            print('Connected to: ', path)
    
    def __enter__(self):
        self.c = self.connection.cursor()
        return self.c.execute(self.command).fetchone()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        print('Connection committed.')
        self.connection.close()
        print('Connection closed.')


#command = 'SELECT * FROM config'
#
#with Database(db_path, command) as values:
#    print(values)
#    
#print(values)

#for item in db_command(db_path, 'SELECT * FROM config'):
#    print(item)

#command = 'UPDATE config SET gpiob2 = 0'
#with Database(db_path, command) as values:
#    print(values)