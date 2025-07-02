test = ' in yek test ast ! '
with open ('test.txt' , 'w') as f :
    f.write (test)
try :
    with open ('test.txt' , 'r') as f :
        answer = f.readline ()
        if answer.strip() == 'in yek test ast !' :
            print ('True')
        else :
            print ('False')

except Exception as e :
    print (' error 404 ! ' , e)
