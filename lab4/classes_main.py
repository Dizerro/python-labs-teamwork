class Pool:

    def __init__ (self, address = None, volume = None, maxpeople = None, enter_price = None, name = None, people_per_day = 0):
        self.__address = address
        self.__volume = volume
        self.__maxpeople = maxpeople
        self.enter_price = enter_price
        self.name = name
        self.people_per_day = people_per_day

    def get_adress(self):
        return self.__address
    
    def get_volume(self):
        return self.__volume
    
    def get_maxpeople(self):
        return self.__maxpeople
    
    def get_people_per_day(self):
        return self.people_per_day
    
    def setattr_people_per_day(self, curent_day_people):
        self.people_per_day = self.people_per_day + curent_day_people 
    
    def __str__(self):
         return f"Pool:{self.__address},{self.__maxpeople} persons,{self.__volume} liters. visiting {self.get_people_per_day()}"

    def __repr__(self):
        return (
        f"Басейн:\n"
        f"name = {self.name}\n"
        f"address = {self.__address}\n"
        f"enter_price = {self.enter_price}\n"
        f"volume = {self.__volume}\n"
        f"maxpeople = {self.__maxpeople}"
            )

    # def __del__(self):
        # print("deleted")


def main():
    # Pool_1 = Pool()
    Pool_2 = Pool("Щирецька 36", 1000, 200, 500, "Три Стихії",) 
    Pool_3 = Pool("Озерна 1", 750, 55 , 550, "KOI", )
    Pool_4 = Pool("Кн. Ольги 1", 100, 20, 99, "басік", )
    Pool_5 = Pool("", 1, 1, 1, "", )

    Pool_4.setattr_people_per_day(10)
    Pool_4.setattr_people_per_day(10)
    Pool_4.setattr_people_per_day(10)
    Pool_4.setattr_people_per_day(10)
    Pool_4.setattr_people_per_day(10)


    # print (repr(Pool_1))
    # print (repr(Pool_2))
    # print (repr(Pool_3))
    # print (repr(Pool_4))
    # print (repr(Pool_5))            

    list = (Pool_2, Pool_3, Pool_4, Pool_5)
    
    _max = list[0]    
    for elem in list:
        if  elem.get_people_per_day() > _max.get_people_per_day():
            _max = elem
    
    print(_max)


main()