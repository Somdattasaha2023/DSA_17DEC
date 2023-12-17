
pos = -1

lower = 0


def binaryser(list, n):
    lower = 0 
    upper = len(list)  - 1 
    while(lower <= upper):
        mid = (lower + upper) // 2
        print('ami', lower,upper,mid)
        if n == list[mid]: 
            globals()['pos'] = mid
            print('am here', lower,upper,mid)
            return True 
        elif n > list[mid]:
            lower = mid + 1
            print('am', lower,upper,mid)
        else :
            upper = mid - 1 

    return False

list = [5,8,76,90,100]

n = 89

if binaryser(list,n):
    print("Found at", pos + 1)
else:
    print("Not Found")
      

    
        
        
    
1, 3, 5, 7, 8 
0, 4

7 