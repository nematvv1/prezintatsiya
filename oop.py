# OOP — bu nima?
#
# OOP — Object Oriented Programming
# ya’ni obyektga yo‘naltirilgan dasturlash.
#
# 👉 Dastur obyektlar orqali quriladi.
# 👉 Har bir obyekt xususiyat (property) va harakat (method) ga ega.
#
# 🟦 OOP ning 4 asosiy tamoyili (eng muhim)
#
# Bu — OOP ga oid eng yodlanadigan qoidalar.
#
# 1️⃣ Encapsulation — ma’lumotni yashirish
# 2️⃣ Inheritance — meros olish
# 3️⃣ Polymorphism — ko‘p shakllilik
# 4️⃣ Abstraction — muhimini ajratish
#
# Endi bitta-bitta sodda qilib tushuntiraman.

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 1) Encapsulation — Kapsulalash
#
# Ma’lumotni ichkariga yashirish.
# Keraksiz joydan o‘zgartirishni oldini olish.

class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password    # private

    def check(self, p):
        return p == self.__password
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 2) Inheritance — Meros olish
#
# Bitta klassdan boshqasi xususiyat va metodlarni oladi.

# 1 single vors
class Parent:
    def display (self):
        print('ota class')

class Child(Parent):
    def show(self):
        print("bola class")


2 multiple
class Parent1:
    def method1(self):
        print('parent1')

class Parent2:
    def method2(self):
        print('parent2')

class Child(Parent1,Parent2):
    pass

# 3 Multilevl

class Grandparent:
    def method1(self):
        print('grandparend')

class Parent(Grandparent):
    def method2(self):
        print('parent')

class Child(Parent):
    def method3(self):
        print('parent')

# 4 ierarxic

class Parent:
    def method(self):
        print('parend')

class Child1(Parent):
    pass

class Child2(Parent):
    pass

# 5 gibrid

class Gybrid:
    def method(self):
        print('gybrid')


class Parent1(Gybrid):
    pass


class Parent2(Gybrid):
    pass


class Child(Parent1, Parent2):
    pass

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 3) Polymorphism — Ko‘p shakllilik
#
# Bir xil metod — turli klasslarda turlicha ishlaydi.

class Cat:
    def sound(self):
        print("Myauuu")

class Dog:
    def sound(self):
        print("Vov-vov")

def make_sound(animal):
    animal.sound()

make_sound(Cat())
make_sound(Dog())

# ,<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Abstraction (abstraktsiya) obyektga yo'naltirilgan dasturlashning (OOP)
# asosiy tamoyillaridan biri
# bo‘lib, murakkab tizimni soddalashtirish uchun muhim bo‘lgan
# xususiyat va funksiyalarni ajratib olishni ta'minlaydi. Abstraktsiya orqali
# foydalanuvchiga faqat kerakli ma'lumotlar taqdim etiladi, qolgan murakkabliklar yashiriladi.
#
# Python'da abstractionni amalga oshirish uchun Abstract
# Base Class (ABC) va @abstractmethod dekoratoridan foydalaniladi.


# Python'da abstraction qanday ishlaydi?
# Abstraktsiya Abstract Base Classlar (ABC) yordamida amalga oshiriladi.
# ABC — bu boshqa klasslar uchun asosiy interfeysni belgilaydigan klass.
# Abstract klass o‘zining aniqlanmagan metodlarini (abstract metodlar)
# voris klasslar tomonidan amalga oshirilishini talab qiladi.
#
# Abstract klasslar to‘g‘ridan-to‘g‘ri obyekt sifatida ishlatilmaydi.


# Abstract klassning asosiy xususiyatlari:
# Abstract klassni yaratish uchun abc modulidan foydalaniladi.
# Abstract klass ichidagi abstract metodlar voris klasslar tomonidan
# majburiy amalga oshirilishi kerak.
# Abstract klassning abstract bo‘lmagan metodlari ham bo‘lishi mumkin.


from abc import ABC, abstractmethod


# Abstract Base Class
class Transport(ABC):
    @abstractmethod
    def harakatlanish(self):
        """Bu metod har bir transport vositasi uchun aniqlanishi kerak"""
        pass

    @abstractmethod
    def yoqilgi_turi(self):
        """Yoqilg‘i turini aniqlovchi abstract metod"""
        pass


# Voris klasslar
class Mashina(Transport):
    def harakatlanish(self):
        return "Yo'lda yuradi"

    def yoqilgi_turi(self):
        return "elakter"


class Samolyot(Transport):
    def harakatlanish(self):
        return "Samolyot havoda uchadi"

    def yoqilgi_turi(self):
        return "Reaktiv yonilg‘i"


# Voris klasslardan foydalanish
mashina = Mashina()
samolyot = Samolyot()
mashina.yoqilgi_turi()
# print(mashina.harakatlanish())  # Mashina yo'lda yuradi
# print(mashina.yoqilgi_turi())  # Benzin

print(samolyot.harakatlanish())  # Samolyot havoda uchadi
print(samolyot.yoqilgi_turi())  # Reaktiv yonilg‘i

# Abstract klassning asosiy xususiyatlari:

# Abstract klassni yaratish uchun abc modulidan foydalaniladi.

# Abstract klass ichidagi abstract metodlar voris
# klasslar tomonidan majburiy amalga oshirilishi kerak.

# Abstract klassning abstract bo‘lmagan metodlari ham bo‘lishi mumkin.

#### Abstract klass farqi

# Abstract klassda esa metodlar to‘liq aniqlanmagan bo‘ladi.
# Bunda metodning faqat nomi va qoidasi aniqlanadi, lekin qanday
# bajarilishi (mazmuni) aniqlanmaydi. Bu shuni anglatadiki, abstract
# klassdan obyekt yaratilmaydi, chunki uning ba'zi metodlari hali amalga oshirilmagan.
#
# Abstract klassning oddiy misoli:

from abc import ABC, abstractmethod


class Hayvon(ABC):  # Abstract klass
    @abstractmethod
    def ovoz_chiqar(self):
        pass


# ovoz_chiqar metodining qanday ishlashi aniq belgilanmagan (pass yozilgan).
# Agar ushbu klassdan obyekt yaratmoqchi bo‘lsangiz, xato chiqadi:

class It(Hayvon):  # Voris klass
    def ovoz_chiqar(self):
        return "Vov-vov!"


it = It()
print(it.ovoz_chiqar())  # Natija: Vov-vov!

# Oddiy klassni to‘liq aniqlash nimani anglatadi?
# Oddiy klassning metodlari:
#
# To‘liq ishlash kodiga ega.
# Klass obyekt sifatida to‘g‘ridan-to‘g‘ri ishlatilishi mumkin.

# Abstract klassda nima to‘liq emas?

# Abstract klassdagi metodlarda ishlash qoidasi faqat aniqlanadi,
# lekin ular qanday bajarilishi noma'lum bo‘ladi. Shu sababli,
# abstract klassdan obyekt yarata olmaysiz.
#
# Abstract metodni to‘liq aniqlash uchun voris klassda u qayta yozilishi kerak:

# Xulosa
# Oddiy klass: Metodlari to‘liq aniqlangan. Bunda har bir metod aniq funksional
# kodga ega bo‘ladi va klassdan obyekt yaratilishi mumkin.

# Abstract klass: Metodlari to‘liq aniqlanmagan. Bunday klassdan obyekt
# yaratib bo‘lmaydi. Voris klasslar abstract metodlarni to‘liq aniqlab, ularni ishlatishga yaroqli qiladi.
