import random
array1 = []
array2 = []
summ = []
for _ in range(10):
    array1.append(random.randint(0, 9))
    array2.append(random.randint(0, 9))
for i in range(10):
    summa = array1[i] + array2[i]
    summ.append(summa)
print("Перший масив:", array1)
print("Другий масив:", array2)
print("Третій мавсив:", summ[::-1]) 
