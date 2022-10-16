a = ["banana", "apple", "grape"]

print(a[0])
print(a[1])
print(a[2])

print(a)

for fruit in a:
    print(fruit)

b = [20, 10, 5]
sum = 0
for num in b:
    print(num)
    sum = sum + num
print(sum)

# 1, 2, 3, 4
range(1, 5)

for i in range(1, 5):
    print(i)

sum2 = 0
for i in range(1, 5):
    #sum2 = sum2 + i
    sum2 += i
print(sum2)

print(list(range(1, 8)))

#sum of multiples of 3
sum3 = 0
for i in range(1, 8):
    if i % 3 == 0:
        sum3 += i
print(sum3)



