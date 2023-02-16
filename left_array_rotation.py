#Left Array Rotation First Approach
# num_rotations=int(input("Enter the number of rotations:\n"))
# def rotLeft(a,d):
#     left_array = a[:num_rotations]
#     right_array=a[num_rotations:]
#     new_array = right_array + left_array
# #   array_no_commas = ''.join(str(new_array).split(','))
#     print(new_array)
#     string_to_array =""
#     for x in new_array:
#        string_to_array += str(x) + " "
#     print(string_to_array)   

# rotLeft(a=[1,2,3,4,5],d=num_rotations) 

# Left Array Rotation Second Approach
num_rotations=int(input("Enter the number of rotations:\n"))
shift_num=[]
def rotLeft(a,d):
    for i in range(1,num_rotations) :
        print(i)   
        shift=a.pop(a[i])
        shift_num.append(shift)
        new_array = a + shift_num
    print(new_array)    
rotLeft(a=[1,2,3,4,5],d=num_rotations)    
