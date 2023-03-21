nums =[0, 1, 0, 1, 2, 1, 1, 0, 0, 0, 0, 1, 1]
n = len(nums)
zero_space_ptr = -1
end_ptr = n - 1
curr = 0 
while curr <= end_ptr:
    if nums[curr] == 0:
        zero_space_ptr += 1
        nums[curr], nums[zero_space_ptr] = nums[zero_space_ptr], nums[curr]
        curr += 1
    elif nums[curr] == 2:
        if nums[end_ptr] < 2:
            nums[curr], nums[end_ptr] = nums[end_ptr], nums[curr]
        end_ptr -= 1
    else:
        curr += 1 
print(nums)
