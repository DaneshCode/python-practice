with open ('1.txt' , 'w') as f :
    f.write ('1024')

with open ('2.txt' , 'w') as f :
    f.write ('2023')

with open ('3.txt' , 'w') as f :
    f.write ('3024')

with open ('4.txt' , 'w') as f :
    f.write ('4024')

with open ('5.txt' , 'w') as f :
    f.write ('1024')


lst = [1,2,3,4,5]

for i in lst :
    try:
        with open ( str (i) + '.txt' , 'r')  as f :
            answer = f.readline ()
            if answer.strip() == '1024' :
                print ( ' the answer provided by no ' , i , ' is right ' )

            else :
                print ( ' the answer provided by no ' , i , ' is wrong ' )

    except Exception as e :
                    print ( ' error ! \n ' , e)
