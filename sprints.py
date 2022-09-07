def myFunction(x):
    z=0
    
    for i in x:
        if (i%2)==0:  
            print (i)
            z += i
            if len(x)>0:
                return z/len(x)
           
        elif (i%2)!=0:
           return max(float(i))
        else:
           return 0
list = 15,12,4
print(myFunction(list))