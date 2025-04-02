class Book:
    title:str
    author:str
    year:int
    genre:str
    pages:int

    def __init__(self,title,author,year,genre,pages):
        self.title=title
        self.author=author
        self.year=year
        self.genre
        self.pages=pages

    def info(self):
        print(f"name:{self.title}")
        print(f"autor:{self.author}")
        print(f"genre:{self.genre}")
    def is_long(self):
        if self.pages>300:
            print("True")
        else:
            print("False")
boook=Book("Преступление и наказание", "Ф.М.Достоевский", 1866,"Драма", 666)
book.info()


class Student:
    name:str
    age:int
    university:str
    year_of_student:int
    gra:float

    def __init__(self,name,age,university,year_of_student,gra):
        self.name=name
        self.age=age
        self.university=university
        self.year_of_student=year_of_student
        self.gra=gra

    def student_year(self):
        print(f"name:{self.name}")
    def is_excellent(self):
        if self.gra>=4.5:
            print("True")
        else:
            print("False")

student=Student("Семен",10,"МГУ",0,4.5)
student.student_year()


class Auto:
    make:str
    model:str
    year:int
    color:str
    mileage:int

    def __init__(self,make,model,year,color,mileage):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
        self.mileage=mileage

    def car_info(self):
        print(f"mark:{self.make}")
        print(f"model:{self.model}")
        print(f"year:{self.year}")
    def needs_service(self):
        if self.mileage>100000:
            print("True")
        else:
            print("False")

auto=Auto("Громила","ультра",1000,"красный",0)
auto.car_info()


class Telefon:
    brand:str
    model:str
    year:int
    battery_capacity:int
    price:float

    def __init__(self,brand,model,year,battery_capacity,price):
        self.brand=brand
        self.model=model
        self.year=year
        self.battery_capacity=battery_capacity
        self.price=price

    def phon_info(self):
        print(f"brand:{self.brand}")
        print(f"model:{self.model}")
        print(f"year:{self.year}")
    def is_expensive(self):
        if self.price>30000:
            print("True")
        else:
            print("False")

telefon=Telefon("Apple","16pro",1,0,100000000000000000)
telefon.is_expensive()
telefon.phon_info()


class Nooyt:
    brand:str
    model:str
    year:int
    ram:int
    price:float

    def __init__(self,brand,model,year,ram,price):
        self.brand=brand
        self.model=model
        self.year=year
        self.ram=ram
        self.price=price

    def laptop_info(self):
        print(f"brand:{self.brand}")
        print(f"model:{self.model}")
        print(f"year:{self.year}")
        print(f"ram{self.ram}")
    def is_high_end(self):
        if self.ram>16 and self.price>50000:
             print("True")
        else:
            print("False")

nooyt=Nooyt("pk 1200","promax1003",10,2,999999999999.99999999999999999999999999999)
nooyt.is_high_end()
nooyt.laptop_info()