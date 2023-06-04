liste1=[1,2,3,4,5]
liste2=list() #liste2 bos bir liste

for i in liste1:
    liste2.append(i)
print(liste2) # liste2=[1, 2, 3, 4, 5]

liste3=[1,2,3,4,5]
liste4=[i for i in liste3]
print(liste4) #[1, 2, 3, 4, 5]

liste=[3,4,5]
liste1=[i*2 for i in liste] #liste deki her bir elemanı 2 ile çarp
print(liste1) #[6, 8, 10]


liste1 = [(1,2),(3,4),(5,6)]
liste2=[i*j for (i,j) in liste1]
print(liste2) # [2, 12, 30]

liste1 = [1,2,3,4,5,6,7,8,9,10]
liste2 = [i for i in liste1 if not (i == 4 or i == 9)]
print(liste2) # [1, 2, 3, 5, 6, 7, 8, 10]

yazi="Python"
liste=[i*3 for i in yazi]
print(liste) # ['PPP', 'yyy', 'ttt', 'hhh', 'ooo', 'nnn']

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste1=list()
for i in liste:
    for x in i:
        liste1.append(x)
print(liste1) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste1=[x for i in liste for x in i]
print(liste1) #liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]





