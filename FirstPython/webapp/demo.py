from DBcm import UseDatabase

global data 
dbconfig = {
    
    'host': '192.168.5.5',
    'user': 'root',
    'password': '123456',
    'database': 'vsearchlogDB',}

with UseDatabase(dbconfig) as cursor:
    _SQL = """show tables"""
    cursor.execute(_SQL)
    data = cursor.fetchall()

print(data)