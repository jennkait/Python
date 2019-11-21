ini_list = [2,4,5,9,3]
elem_to_find = 9
res1 = any(elem_to_find in sublist for sublist in ini_list)
print(str(res1))