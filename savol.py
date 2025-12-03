# class CAT:
#     def sound(self):
#         print('myau')
#
# class DOG:
#     def sound(self):
#         print('vav')
#
# def speak(animal):
#     animal.sound()
#
# class User:
#     def __init__(self,name,password):
#         self.name=name
#         self.__password=password
#     def get_password(self):
#         return self.__password
#
# U=User('asad',12)
# print(U.get_password())
#
# class User:
#     def __init__(self,name, password):
#         self.name=name
#         self._password=password
#
# user=User('asad',2324)
# print(user._password)

#
# class Student:
#     def __init__(self,name,password):
#         self.name=name
#         self.__password=password
#     @property
#     def get_pass(self):
#         return self.__password
#     @get_pass.setter
#     def get_pass(self,valu):
#         if valu>0:
#             self.__password=valu
#
# u = Student("asad", 1213)
#
# print(u.get_pass)     # getter — qavs YO‘Q!
# u.get_pass = 9999     # setter — oddiy qiymat berish
# print(u.get_pass)

#
# class User:
#     count=0
#     def __init__(self,name):
#         self.name=name
#         User.count+=1
#
#     @classmethod
#     def how(cls):
#         return cls.count
#
# print(User.how())  # 0
# a = User("A")
# b = User("B")
# print(User.how())  # 2
#
#
# class Person:
#     count=0
#     def __init__(self,name):
#         self.name=name
#         Person.count+=1
#
#     @classmethod
#     def his(cls):
#         return cls.count
# p=Person('a')
# print(Person.his())
#
# class Mathem:
#     @staticmethod
#     def math(a,b):
#         return a+b
# print(Mathem.math(2,4))


from abc import ABC,abstractmethod

class Transport(ABC):
    @abstractmethod
    def harakatlanish(self):
        """Nimada harakatlanadi"""
        pass


    def yoqilgi(self):
        """nimada yuradi"""
        pass

class Samalyot(Transport):
    def harakatlanish(self):
        return 'havoda'




