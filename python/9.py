amir = 'mamad,is,gozoo'

with open ('amir.txt' , 'w') as f :
    f.write (amir)    


with open ('amir.txt' , 'r') as f :
    for line in f :
        amir = line.split(',')
    for amir in amir :
        print (amir)
