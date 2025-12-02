# 1. Class (klass) — bu nima?
#
# Class — bu shablon (чертёж).
# Undan obyektlar (object) yaratiladi.
#
# Oddiy qilib:
#
# Class → Qurilish chizmasi
#
# Object → Shu chizma bo‘yicha qurilgan uy

# MISOL
class Person:
    pass
# Bu Person degan klass.
# Undan obyekt yaratamiz:

p = Person()

# >>>>>>>>>>>>>>>>>>>>
# 2. Class nima uchun kerak?
# ✔ Kodni tartibli qilish uchun
# ✔ Bir xil xususiyatdagi narsalarni bitta joyga jamlash uchun
# ✔ Katta loyihalarda boshqarishni osonlashtirish uchun
# ✔ Obyektlar yaratish uchun
#
# Masalan, sizda 100 ta odam bo‘lsa — 100 ta dictionary yozish shart emas.
# Bitta class qilib, undan 100 ta obyekt yaratish yetadi.

# >>>>>>>>>>>>>>>>>>>
# 3. Class tarkibi (asosiy elementlar)
# 1) Property (xususiyatlar) — o'zgaruvchilar
# 2) Method (metodlar) — funksiyalar
# 3) init() — konstruktor


# >>>>>>>>>>>>>>>>>>>>>>>>
# 4. init() — konstruktor
#
# Obyekt yaratilganda avtomatik ishga tushadi.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# >>>>>>>>>>>>>>>>>>>>>>>>>
# 5. self nima?
#
# self — obyektning o‘zini bildiradi.
# Java yoki C++ dagi this bilan bir xil.
#
# Har bir obyektning o‘z:
#
# name
#
# age
#
# phone
#
# boshqa obyektlardan mustaqil bo‘ladi.


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 6. Class ichida funksiyalar (metodlar)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Men {self.name}, yoshim {self.age}")
p = Person("Ali", 20)
p.introduce()

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# CLASS METHODLARI
# 1) INSTANCE METHOD (oddiy metod)
#
# Eng ko‘p ishlatiladigani.
# Har doim self qabul qiladi.
#
# 👉 Obyektga tegishli.
# 👉 Obyekt ichidagi ma’lumot bilan ishlaydi.

class A:
    def instance_method(self):
        print("Bu instance method")


# 2) CLASS METHOD (klassga tegishli metod)
#
# @classmethod dekoratori bilan yoziladi.
# Parametr sifatida cls qabul qiladi.
#
# 👉 Klassning o‘ziga tegishli (obyektga emas).
# 👉 Klass bo‘yicha umumiy ma’lumotlar bilan ishlaydi.

class A:
    count = 0

    @classmethod
    def class_method(cls):
        print("Bu class method")

# 3) STATIC METHOD (mustaqil metod)
#
# @staticmethod dekoratori bilan yoziladi.
# Hech qanday self yoki cls olmaydi.
#
# 👉 Oddiy funksiya, lekin klass ichida joylashgan.
# 👉 Klass bilan bog‘liq mantiq bo‘lsa — class ichida saqlanadi.

class A:
    @staticmethod
    def static_method():
        print("Bu static method")
