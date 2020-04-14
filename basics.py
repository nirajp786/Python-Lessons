#cdefgab
s = "abcd"
l = 4
r = 2

shifts = 0
print(s)

if(l > r):
    shifts = l-r
    left_string = s[shifts:]
    temp = s[:shifts]
    print(temp)
    print(left_string)
    left_string = left_string + temp
    print(left_string)
else:
    shifts = r-l
    shifts = shifts * -1
    right_string = s[shifts:]
    temp = s[:shifts]
    print(temp)
    print(right_string)
    print(right_string+temp)
    

# left_string = s[l:]
# print(left_string)
# left_string = left_string + s[:l]
# print(left_string)

# right_string = left_string[r:]
# print(right_string)
# print(left_string[:r])
# right_string = right_string + left_string[:r]
# print(right_string)