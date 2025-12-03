# 1-classni tushuntirib bering 2- kanstruktorlarni tushuntiring
# 3- class metodlarini tushuntirib bering 4- vorislikni tushuntirib bering
# 5- polimarfizmni tushuntirib bering 6- inkapsulation nima
# 7-aksis modifayillarni tushuntirib bering 8- gettr settirni tushuntirib bering
# 9- propertiyni tushuntirib bering 10-abstrakt clasni tushuntirib bering
# 11- abstrakt metodni tushuntirib bering

# >>>>>>>>JAVOBLAR<<<<<<<<<<<<<
# 1
# class bu shablon undan objektlar yaratiladi

# 2
# kanstruktor abyekt yaratilganda avftomatik ishlaydigan method
class CAR:
    def __init__(self,model,year):
        self.model=model
        self.year=year


# 3
# class methodlari 3 ta boladi

# 1- instanse method
def info(self):
    print(self.model)

# 2) Class Method
#
# Klassga tegishli.
# @classmethod bilan yoziladi, cls qabul qiladi.
@classmethod
def say_hi(cls):
    print("Hi from class")

# 3) Static Method
#
# Klassga ham, obyektga ham bog‘liq emas.
# @staticmethod bilan yoziladi.
@staticmethod
def add(a, b):
    return a + b

# >>>>>>>>>>>>>>>>>>>>>>>>
# 4- bitta class malu,otini boshqa clasda ishlata olishi (bir clas boshqa class xsusiyatlarini olishi)

# 1 single vors
# bitta ota bitta bola
# 2 multiple
# bitta sup class bir nechta super class

# 3 Multilevl
# bur biridan vors olib ketaveradi

# 4 ierarxic
# bitta ota bir nechta bola

# 5 gibrid

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 5. Polimorfizm (Polymorphism)
#
# Bir xil metod — turli klasslarda turlicha ishlaydi.

class Cat:
    def sound(self):
        print("Myau")

class Dog:
    def sound(self):
        print("Vov")

def speak(animal):
    animal.sound()

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 6. Inkapsulyatsiya (Encapsulation)
#
# Ma’lumotni yashirish (private qilish).
class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    def get_password(self):
        return self.__password

u = User("1234")
print(u.get_password())

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 7. Akses modifikatorlar (Access Modifiers)
#
# Python’da 3 xil ko‘rinishda ishlaydi:

# 1) public
#
# Hamma joydan ko‘rinadi
self.name

# 2) protected
#
# Bitta _ bilan: tavsiya — ichkarida ishlatiladi
self._balance

# 3) private
#
# Ikki __ bilan: faqat class ichida ishlaydi

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 8. Getter va Setter
#
# Yashirilgan xususiyatlarga nazorat bilan kirish.

class User:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if len(new_name) > 2:
            self.__name = new_name

# >>>>>>>>>>>>>>>>>>>>>>>>>
# 9. @property — getter/setter ning elegant ko‘rinishi
class User:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 0 < value < 120:
            self.__age = value
u = User(20)
u.age = 30        # setter
print(u.age)      # getter


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 10. Abstrakt class (Abstract class)
#
# Bu — faqat g‘oya beradigan klass, to‘liq ishlamaydi.
# Undan obyekt yaratib bo‘lmaydi.
from abc import ABC

class Animal(ABC):
    pass

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 11. Abstrakt metod
#
# Meros olgan klass yozishi shart bo‘lgan metod.
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Vov")


