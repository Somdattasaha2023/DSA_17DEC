def sort(nums) :
    for i in range(len(nums)-1,0,-1):  # ist is 2
        print("i :" , i)
        for j in range(i) :
             
            if nums[j]>nums[j + 1]:  
                print("i, j " ,i,j)
 #       after 1st i 3 , last element is placed at the last positions -- 3 5 2 , 3 2 5, 
                                    # after 2nd i 2 , 1st and 2 eleemnt is only targeted : 2 3 5                                         
                temps = nums[j]
                nums[j] = nums[ j + 1]
                nums[j + 1] = temps

            
        
    
nums = [ 5,3,2]
sort(nums)
print(nums)

for k in range(2,0,-1):
     print("hello", k)