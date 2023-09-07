from random import randint

array1 = []
array2 = []
array3 = []

for i in range(10):
    array1.append(randint(0, 9))
    array2.append(randint(0, 9))

carry = 0
for i in range(9, -1, -1):
    total = array1[i] + array2[i] + carry
    carry = total // 10
    array3.insert(0, total % 10)

if carry > 0:
    array3.insert(0, carry)

print(f"Перший масив: {array1}")
print(f"Другий масив:{array2}")
print(f"сума: {array3}")
