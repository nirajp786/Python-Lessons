#Author: Nirajkumar Patel
#Date: 2020-01-15
#Description: Have two strings and create a new string which has characters iterated from both one by one
#Example: String 1: ABC, String 2: DEF, Output: ADBECF. The longer string's remaning characters get added on as well. 

#two example string
str1 = "ABCDEFDUYKM"
str2 = "GHIJKLPG"
#empty string
list1 = []

#cases where if the length of the strings were the same
if(len(str1) == len(str2)):
    #a loop that gets character of each string and run till the len of the shortest string
    for a, b in zip(str1, str2):
        #appends the character to the list
        list1.append(a)
        list1.append(b)
    
    #joins the list to form a string
    str3 = ''.join(list1)
    #outputs the string
    print(str3)
    
elif(len(str1) < len(str2)):
    for a, b in zip(str1, str2):
        list1.append(a)
        list1.append(b)
    
    len2 = len(str2) - len(str1)
    len2 = len2 * -1
    
    remaing_words = str2[len2:]
    list1.append(remaing_words)
    str3 = ''.join(list1)
    print(str3)
    
elif(len(str1) > len(str2)):
    for a, b in zip(str1, str2):
        list1.append(a)
        list1.append(b)
    
    len2 = len(str1) - len(str2)
    len2 = len2 * -1
    
    remaing_words = str1[len2:]
    list1.append(remaing_words)
    str3 = ''.join(list1)
    print(str3)
