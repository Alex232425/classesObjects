class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закритые соединение с БД")

    def read(self):
        return "Данные с БД"

    def write(self, data):
        print(f"запись в БД {data}")


db = DataBase("петро", 123, 345)
db2 = DataBase("петр", 654, 389)

print(id(db), id(db2))
