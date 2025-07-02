class Person :
    def __init__ (self , name , age , num) :
        self.name = name
        self.age = age
        self.num = num

    def __str__ (self) :
        return f'{self.name} {self.age} {self.num}'


class Student (Person) :
    def welcome (self) :
        print (' Hello ', self.name , self.age , ' welcome to the class room in my kir uni ')



p1 = Person ('Dani_Kh' , 18 , 2283)

s1 = Student ('mamad' , 18 , 2299)
