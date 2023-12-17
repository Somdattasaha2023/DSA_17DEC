pos = -1

def search(list,n) :
    
    i = 0 
    while (i<len(list)) :
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
        
    return False

list = [5,8,76,90,4]

n = 4

if search(list,n):
    print("Found at", pos + 1)
else:
    print("Not Found")
        
        
    
        
    
