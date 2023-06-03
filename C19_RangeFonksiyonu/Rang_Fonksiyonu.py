range(0,20)
print(*range(0,20)) # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

print(*range(20)) # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

print(*range(1,100,2)) #1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 ......

print(*range(20,0,-1)) #20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1

liste=[1,2,3,4,5]
for i in liste:
    print(i)

for i in range(1,6):  # yukarıdaki ile aynı sonucu verdi.
    print(i)

for i in range(1,10):
    print("* " * i )