import sys
# import math



n = int(input())

# def recurse(n):
count =0
num =1
den = 1
for k in range(n):
    # print(k)
    temp_num = num
    temp_den = den
    num = 2*temp_den +temp_num
    den = temp_den + temp_num
    # print(len(str(num)))
    # print(num)
    # print(len(str(den)))
    if len(str(num)) > len(str(den)):
        print(k+1)
    
# recurse(n)
