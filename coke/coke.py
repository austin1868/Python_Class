cost = 50
i = 0

while i < cost :
    print("Amount Due: " + str(cost-i) )
    new = int(input("Insert Coin: "))
    if new in [5, 10, 25, 50]:
        i += new

print("Change Owed: " + str(i-cost))