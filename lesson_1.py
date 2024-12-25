# my_list = [1,2,3,4,5]
# i = 0
# while i < len(my_list):
#     print (my_list[i])
#     i = i *i


# a = ['apple','banana','orange']
#
# for i in a :
#     print (i)



# a = ['1,2,3,4,5']
#
# for i in a:
#     print (i)

# for i in range(1,10+1,1):
#     print (i)

# i = 0
# while i <= 10 :
#     print(f"цифры {i}")
#     i = i + 1

# while True:
#     user_input = input ("ведите'stop'для выхода")
#     if user_input =="stop":
#         print("программа завершено")
#         break
#         print ("попробуйте еше")

# list = ["Moskow,Tashkent,bishkek"]
#
# a = 'Moskow'
# a  in list
# print (f"cтрана найдена {a}")

# a = ['azamat','manas','ruslan']
# b = ['dog','cat','lion']
# if a + b :
#  print (a + b)

# a = [3,456,35,455,245,24,145,35,]
# for i in a :
#     if i > 10 :
#         print (i)

# a = [3,456,35,455,245,24,145,35,]
# b = []
# i = 0
# while i < len(a):
#     if a [i] > 10 :
#         b.append((a[i]))
#         i += 1
# print ("элемент больше 10",b)

# a = int(input('a'))
# b = int(input('b'))
# for i in range (a,b+1):
#     print(i)





# жуп сандар  2, 4,6 , 8
# так сан   1, 3,5, 7

#
# my_list = []
#
# i = 0
# while i < 100:
#     my_list.append(i)
#     i = i + 1
#     print(f"удалит кылуудан алдын{my_list}")
#
#
# i = 1
# while i <100:
#     if i % 2 == 8:
#         my_list.remove(i)
#         i = i + 1
#         print(f"удалит кылуудан алдын{my_list}")

# my_list = []

# for i in range (100):
#      my_list.append(i)
#      print(f"удалит кылуудан алдын{my_list}")
#
# my_list = []
# for i in range ( 100+1 ):
#          my_list.remove(i)
# print(f"удалит кылуудан алдын{my_list}")

# list = [2,1,4,3,]
# a = 0
# for a in list :
#     a +=1
# print(a)
#
# myset = {1,2,1,1,2,2}
# myset.add(434)
# print(myset.clear())


# mydic = {11:48, 5:9 , 3:22}
# print(mydic[5])

# a = {
#  "brend": "hyundai",
#   "model" "stinger"
#   "year": 2018
# }
# a.pop('model')
# print(a)

# mydic = {}
# for i in range (1,101):
#    mydic [i] = i
# print(mydic)


# mydic = {}
#
# for i in range ( 2,100,2):
#    mydic [i] = i + 1
# print (mydic)

# mydic = {
#    'apple':'яблоко',
#    'banana':'банан',
#    'cherry':'вищня'
# }
# a = input("ведите слово на англиском")
# translation = mydic.get(a,"cлово не найдено")
# print(translation)


# people = [
#     {"name":"tom","age":39,"company":"supercorp","languages": ["payton","javaScript"]},
#     {"name":"bob","age":43,"company":"bigcorp","languages": ['payton',"C++","C"]},
#     {"name":"sam","age":28,"company":"littlecorp","langeages":["payton","Java"]},
# ]
# search_name = input("ведите имя человека").strip()
# person_data = next((person for person in people if person['name'].lower()== search_name.lower()),None)
# if person_data :
#     print(f"данные о {search_name}"
#     f"{person_data}")
# else:
#     print(f"человека не сушествует {search_name}")


# a = {"name":"sam","age":28,"company":"littlecorp","langeages":["payton","Java"]}
#
# b = input("ведите имя челoвека" )
# if b in a :
#     print (f"значение этого ключа :{a}[b]")
# else:
#     print ('не найден')

# a = {
#     "понедельник":1,
#     "вторник":2,
#     "среда":3,
#     "четверг":4,
#     "пятница":5,
#     "суббота":6,
#     "воскресеье":7,
# }
# print(a)

# a = { 2 :3 , 44:5 ,75 :8}
# result =a.clear()
# print (a)

# a = {2:4,6:8,9:12 }
# print (a.values())

# a = {"Dima" :40,"uson":15,"esentur":17}
# for i in a :
#     a[i] += 5
# print(a)

# i = 0
#
# while i <= 100:
#     print(i)
#     i = i +1

# i = 10
# while i <= 10000:
#   print(i)
#   i = i +2


# def artur(name):
#     return f'{name} hello'
# print((artur("artur")))


# def add_number (a,b):
#     return a +b
# result= add_number(2 , 6)
# print(result)

# def artur (name,age):
# #     return f'{name,age} жаш'
# # print (artur("japar",15))

# def artur (surname,name,age):
#     return f'{surname,name,age} жаш'
# print (artur("jeenbekov","japar",15))

# def artur (a,b):
#     return a + b
# result = artur(5,5)
# b = artur (15, 15)
# print(result)
# print(b)



