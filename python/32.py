class Programmer :
    def  __init__ (Self , Name , Age , Contry) :
        Self.Name = Name
        Self.Age = Age
        Self.Contry = Contry

    def __str__ (Self) :
        return f'{Self.Name} {Self.Age } {Self.Contry}'

p1 = Programmer ('Dani' , 18 , 'iran')
p2 = Programmer ('Menashe' , 18 , 'israel')

print(p1)
print(p2)
