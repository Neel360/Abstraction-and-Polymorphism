class England():
    def capital(self):
        print("London is the capital of England.")

    def language(self):
        print("English is the official language of England.")

    def development(self):
        print("England is developed.")

class Scotland():
    def capital(self):
        print("Edinburgh is the capital of Scotland.")

    def language(self):
        print("English and Gaelic are spoken in Scotland.")

    def development(self):
        print("Scotland is developed.")

class Wales():
    def capital(self):
        print("Cardiff is the capital of Wales.")

    def language(self):
        print("English and Welsh are spoken in Wales.")

    def development(self):
        print("Wales is developed.")

obj_eng = England()
obj_wal = Wales()
obj_sco = Scotland()

for country in (obj_eng, obj_wal, obj_sco):
    country.capital()
    country.language()
    country.development()


