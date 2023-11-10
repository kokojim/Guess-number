import random
a = (random.randint(1,10))
n = 0
b = int(input("猜一個數字 1 to 10 : "))
while a != b:
    if a < b:
        print("太高，再一次")
        b = int(input("猜一個數字 1 to 10 : "))
        n += 1
    if a > b:
        print("太低，再一次")
        b = int(input("猜一個數字 1 to 10 : "))
        n += 1
if a == b:
    print("恭喜答對")
    print("試了",int(n+1),"次")
    c = int(input())#做暫停
