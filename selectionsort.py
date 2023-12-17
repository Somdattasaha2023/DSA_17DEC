def sort(nums) :
    for i in range(len(nums)-1) :
        print("in outer" , i)
        print(nums)
        minpos  = i 
        for j in range(i+1,len(nums)) :
            print("in inner:", j )
            if nums[j] < nums[minpos]:
                minpos = j
                flag = 1 
                print("minpos: ",minpos)
        
        if flag:
            temp = nums[i]
            nums[i] = nums[minpos]
            nums[minpos] = temp
            
         
         
         
nums = [ 4, 8, 1,65,43,99,100,908,0 ]
sort(nums) 
print(nums)     