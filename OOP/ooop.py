# ############################## incapsulation ################################
#
# class Car:
#     def __init__(self, model, marka, color):
#         self.__model = model
#         self.__marka = marka
#         self.__color = color
#
#
#
#     def get_model(self):
#         return self.__model
#
#     def get_marka(self):
#         return self.__marka
#
#
#
#     def set_model(self, new_model):
#         self.__model = new_model
#
#     def set_color(self, new_color):
#         self.__color = new_color
#
#     def start(self):
#         print(f'{self.__model}  Car is startig')
#     def move(self):
#         print(f"{self.__model}  Car is moving")
#     def stop(self):
#         print(f"{self.__model}  Car is stoping")
#
#     def display_info(self):
#         print(f"model: {self.__model}\n"
#               f'marka: {self.__marka}\n'
#               f'color:  {self.__color}\n'
#               )
#
#
# mers = Car('Mers','SLS AMG', 'black')
# mers.set_color('yellow')
# mers.set_model('Mazda')
#
#
# mers.display_info()


class Gamepers:
    def __init__(self, name, age,pol,ves,rost):
        self.__name = name
        self.__age = age
        self.__pol = pol
        self.__ves = ves
        self.__rost = rost



#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def set_pol(self, new_pol):
#            self.__pol = new_pol
#     def set_rost(self, new_rost):
#         self.__rost = new_rost
#
#     def start(self):
#         print(f'{self.__name}  pers is startig')
#     def move(self):
#         print(f"{self.__age}  pers is moving")
#     def stop(self):
#         print(f"{self.__pol}  pers is stoping")
#
#     def display_info(self):
#          print(f"name: {self.__name}\n"
#                f'age: {self.__age}\n'
#                f'pol:  {self.__pol}\n'
#                )
#
# pers = Gamepers('Martis','18', 'male','75','172')
# print(pers.get_age())
# pers.display_info()
