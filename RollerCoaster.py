# -*- coding: utf-8 -*-


def rollercoaster(a):
    '''
    This function takes in an array and convert it into a
    roller coaster array.  An array B[1 . . . n]is called a roller coaster if 
    B[1] < B[2], B[2] > B[3], B[3] < B[4]
    and so on. More formally: B[2i] > B[2i + 1] and B[2i − 1] < B[2i] for all i.
    
    The pseudo code for the solution is given below. 
    
    RollerCoaster(a[1.....n])
        # We will take the range from zero to length of n - 1. 
        for i in range(1, n-1):
            # Here we access the next element a[i+1] thats why the range is from 1 to n-1,
            # so that we dont go array out of bounds. 
            if i%2 == 1:
                if a[i] > a[i+1]:  
                    swap(a[i], a[i+1]
            if i%2 == 0:
                if a[i] < a[i+1]:
                    swap(a[i],a[i+1])
        return a                    
                
    '''
    for i in range(0,len(a)-1):
        if i%2 == 0 :
            if a[i] > a[i+1]:
            # In the next three lines I am essentially swapping the values. 
            # In the pseudo code, you can just write swap(a[0], a[1]) 
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
        if i%2 == 1:
            if a[i] < a[i+1]:
                temp = a[i+1]
                a[i+1] = a[i]
                a[i] = temp   
    return a                     



        