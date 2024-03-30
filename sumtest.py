#!/usr/bin/env python3
a = [1,2,3,4,5,6,7,8,9,10,14]
num = int(input("A number: "))
for x in a:
    for y in a:
        if x+y==num:
            print(str(a[x-1])+ " " +str(a[y-1]))
