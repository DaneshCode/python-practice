class Student :
    def __init__ (Self , Fname , Lname , Age , City , Number) :
        Self.Fname = Fname
        Self.Lname = Lname
        Self.Age = Age
        Self.City = City
        Self.Number = Number


    def __str__ (Self) :
        return f'{Self.Fname} {Self.Lname} {Self.Age} {Self.City} {Self.Number}'


S1 = Student ('Dani' , 'Khodadad' , 18 , 'Shiraz' , 2283)
S2 = Student ('Amir' , 'Amiri' , 29 , 'Yazd', 2285)
S3 = Student ('Reza' , 'Ahmadi', 11 , 'Tehran', 2296)


print(S1)
print(S2)
print (S3)
