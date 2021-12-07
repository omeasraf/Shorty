import sqlite3, datetime


class URL:
    def __init__(self, url:str, id: str, date:datetime.datetime) -> None:
        self.url = url
        self.id = id
        self.date = date
    
    def toString(self) -> dict:
        data = {
            "url": self.url,
            "id": self.id,
            "date": int(self.date.timestamp() * 1000)
        }
        return data

class Database:
    def __init__(self, name:str) -> None:
        self.conn = sqlite3.connect(name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def createDB(self) -> None:
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Shortened (url text, id text, date text)''')
        self.conn.commit()
    
    def create(self, url:str, id: str) -> None:
        self.cursor.execute(f'''INSERT INTO Shortened (url,id,date) VALUES ('{url}', '{id}', datetime('now'))''')
        self.conn.commit()

    def find(self, url:str, id:bool = False) -> URL:
        if id:
            self.cursor.execute(f'''SELECT url,id,date  FROM Shortened WHERE id = '{url}' ''')
        else:
            self.cursor.execute(f'''SELECT url,id,date  FROM Shortened WHERE url = '{url}' ''')
        data = self.cursor.fetchmany(1)
        if len(data) >= 1:
            return URL(data[0][0], data[0][1], datetime.datetime.strptime(data[0][2], "%Y-%m-%d %H:%M:%S"))
        else:
            return None
        
    
    def close(self) -> None:
        self.conn.commit()
        self.cursor.close()

